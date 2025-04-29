class MyManage:
  def __enter__(self):
    print('进入 with 语句')
    return self
  def __exit__(self, exc_type, exc_val, exc_tb):
    print('离开 with 语句')
    return False

with MyManage() as m:
    print(m)