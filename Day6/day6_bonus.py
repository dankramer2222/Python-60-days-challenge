contents = ['blablabla jufrhgr euhghure.', 'hygyrfhgye djhgdhjgh eufdfu.', 'sufhfs feuhfgh.']
filenames = ["doc.txt", 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f'files/{filename}','w')
    file.write(content)