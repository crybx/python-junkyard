import urllib.request

chapter = "Chapter 55 - Conversation (2)"
url1 = "https://media.reaperscans.com/file"
url2 = "4SRBHm/comics/6512f39c-67dc-4de3-bdd1-92a84cfd6284/chapters/464de1d2-b825-48ca-81bb-90060cc39f92/"
url3 = ".jpg"
chapter_num = 1

get_next = True
while get_next:
    try:
        ch_num_str = str(chapter_num)
        filename = str(ch_num_str.zfill(2)) + url3
        url = url1 + url2 + filename
        urllib.request.urlretrieve(url, filename)
    except Exception as e:
        get_next = False
        print(f'error on {chapter_num}: {e}')

    chapter_num += 1
