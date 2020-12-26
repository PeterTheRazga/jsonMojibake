text = open(os.path.join(subdir, file), encoding='utf-8')
conversations.append(json.load(text))