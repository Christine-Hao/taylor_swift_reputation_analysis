import csv

# 定义一个函数来过滤包含特定关键词的文章
def filter_articles_by_keyword(csv_filename, keyword):
    filtered_articles = []

    # 打开CSV文件并读取内容
    with open(csv_filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 跳过表头

        # 遍历CSV文件中的每一行
        for row in reader:
            title, standfirst = row
            # 检查标题或小标题是否包含关键词
            if keyword.lower() in title.lower() or keyword.lower() in standfirst.lower():
                filtered_articles.append((title, standfirst))

    return filtered_articles

# 定义CSV文件名和关键词
csv_filename = 'halfyear.csv'  # 替换为您的CSV文件路径
keyword = 'Taylor Swift'

# 过滤文章
taylor_swift_articles = filter_articles_by_keyword(csv_filename, keyword)

# 将过滤后的文章保存到新的CSV文件
output_csv_filename = 'filtered_taylor_swift_articles.csv'  # 新的CSV文件路径

with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Standfirst'])  # 写入表头
    writer.writerows(taylor_swift_articles)  # 写入过滤后的文章

# 打印结果
for article in taylor_swift_articles:
    print(f"Title: {article[0]}, Standfirst: {article[1]}")
    print("----------------------------------------------------")
    
output_txt_filename = 'filtered_taylor_swift_articles_taylor_swift_articles.txt'  # 新的文本文件路径

with open(output_txt_filename, 'w', encoding='utf-8') as txt_file:
    for article in taylor_swift_articles:
        txt_file.write(f"Title: {article[0]},\nStandfirst: {article[1]}\n")
        txt_file.write("----------------------------------------------------\n")

output_txt_filename