from concurrent.futures import ThreadPoolExecutor as ThreadPool, ProcessPoolExecutor as ProcessPool, wait, ALL_COMPLETED
import threading
import os, sys, json, requests, time, math
import uuid
import multi_url

# 进程池内进程最大数量 !!谨慎配置 不当会影响性能
process_cnt = 6
# 线程池内线程最大数量 !!谨慎配置 不当会影响性能
thread_cnt = 12

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'
}

jsonPath = './json'
videoPath = './video'


def downloadVideo(download_url, name, store_path):
    resp = requests.get(url=download_url, headers=headers)
    with open('{}/{}.mp4'.format(store_path, name), 'wb') as video_f:
        video_f.write(resp.content)
        video_f.close()
        print(
            'process id: {} \nthread id: {} \nname: {} \nurl: {}'.format(os.getpid(), threading.current_thread().ident, video_f.name, download_url))


# 给进程分配任务
def new_process(tasklist, store_path):
    thread_tasks = []
    with ThreadPool(thread_cnt) as thread_pool:
        for task in tasklist:
            data = {
                'name': task['desc'].replace('\n', '') if task['desc'] != "" else uuid.uuid1().hex,
                'url': task['video']['play_addr']['url_list'][0],
                'storePath': store_path
            }
            thread_tasks.append(thread_pool.submit(downloadVideo, data['url'], data['name'], store_path))
    # wait(thread_tasks, return_when=ALL_COMPLETED)


if __name__ == '__main__':
    # 没输入参数
    if len(sys.argv) != 2:
        sys.exit()

    url = sys.argv[1]

    if os.path.exists('json') is False:
        os.mkdir('json')
    if os.path.exists('video') is False:
        os.mkdir('video')

    tstart = time.time()
    sec_uid = multi_url.getUrl(url)
    storePath = '{}/{}'.format(videoPath, sec_uid)
    if os.path.exists(storePath) is False:
        os.mkdir(storePath)

    process_tasks = []

    process_pool = ProcessPool(process_cnt)

    path = os.path.abspath('{}/{}'.format(jsonPath, sec_uid))
    for f in os.listdir(path):
        listdata = []
        with open("{}/{}".format(path, f), 'r', encoding='utf-8') as file_obj:
            content = file_obj.read()
            # 读取json文件
            jsondata = json.loads(content)
            listdata = jsondata['aweme_list']
            file_obj.close()

        lstart = 0
        # 每个核心分配的任务数
        step = math.ceil(len(listdata) / process_cnt)
        if step >= 6:
            # 无法整除
            mod = int(len(listdata)) % step
            for i in range(process_cnt):
                if lstart + step < len(listdata):
                    process_tasks.append(process_pool.submit(new_process, listdata[lstart: lstart + step], storePath))
                    lstart += step
                else:
                    process_tasks.append(process_pool.submit(new_process, listdata[lstart: lstart + mod], storePath))
        # 如果总数小于6个 只用单核
        else:
            process_tasks.append(process_pool.submit(new_process, listdata, storePath))


    wait(process_tasks)
    print('Your video task has Done!\nruntime: {}s'.format(round(time.time() - tstart, 2)))
    os.system("pause")
