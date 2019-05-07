'''
2つのリストを取りなさい、例えばこれら2つを言う：

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

リスト間で共通の要素のみを含むリストを返すプログラムを作成します（重複はしません）。
プログラムが異なるサイズの2つのリストで動作することを確認してください。

'''

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    same_number = list(set(a) & set(b))
    print(same_number)


if __name__ == '__main__':
    main()
