import os

def search_files(dirname):
  try:
    filenames = os.listdir(dirname)

    for filename in filenames:
      full_filename = os.path.join(dirname, filename)

      if os.path.isdir(full_filename): #디렉토리인지 파일인지 구별
        search_files(full_filename) #디렉이면 search를 재귀호출하여 그 디렉을 파고 듬
      else:
        ext = os.path.splitext(full_filename)[-1] #확장자
        if ext == '.py':
          print(full_filename)
  except PermissionError:
    pass


search_files("/home/runner/Zeus")
