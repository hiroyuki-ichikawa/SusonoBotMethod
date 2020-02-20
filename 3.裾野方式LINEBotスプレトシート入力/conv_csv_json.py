# coding:utf-8
# 市川博之（Hiroyuki Ichikawa） 2019/5/3
# var 1.10 LINE用の基本コマンド対応
#
#
import csv
import random
import sys

args = sys.argv

filename = './' + args[1]

with open(filename, 'r') as f:
	reader = csv.reader(f)
	header = next(reader)  # 読み込み

	for row in reader:
		print(row[1])       # intentsのファイル名、名前
		fname  = "./intents/" + row[1] + ".json"
		fname2 = "./intents/" + row[1] + "_usersays_ja.json"
		print(fname)

		# Flag
		LineFlag = 0

		# intentsファイル
		out_f = open(fname,'w',encoding="utf-8_sig")
		id = "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(4)])) + "-" +"".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(6)]))
		#out_f.write( id )
		out_f.write('{\n')
		str = "\t\"id\" : \"" + id + "\",\n"
		out_f.write(str)
		str = "\t\"name\" : \"" + row[1] + "\",\n"
		out_f.write(str)
		str = "\t\"auto\" : true,\n"
		out_f.write(str)
		str = "\t\"contexts\" : [],\n"
		out_f.write(str)
		str = "\t\"responses\" : [\n"
		out_f.write(str)
		str = "\t\t{"
		out_f.write(str)
		str = "\t\t\"resetContexts\": false,\n"
		out_f.write(str)
		str = "\t\t\"affectedContexts\": [],\n"
		out_f.write(str)
		str = "\t\t\"parameters\": [],\n"
		out_f.write(str)
		str = "\t\t\"messages\": [,\n"
		out_f.write(str)
		str = "\t\t\t{\n"			# 通常メッセージの始まり
		out_f.write(str)
		str = "\t\t\t\"type\" : 0, \"lang\" : \"ja\", \"speech\" : \"" + row[2] + "\"\n"
		out_f.write(str)
		str = "\t\t\t},{\n"
		out_f.write(str)
		str = "\t\t\t\"type\" : 0, \"lang\" : \"ja\", \"speech\" : []\n"
		out_f.write(str)			# LINE用に追加するならこの行の次に入れる
		if len(row[6])>0:			# LINE用の文字列
			LineFlag = 1
			str = "\t\t\t},{\n"
			out_f.write(str)
			str = "\t\t\t\"type\" : 0, \"platform\" : \"line\", \"lang\" : \"ja\", \"speech\" : \"" + row[6] + "\"\n"
			out_f.write(str)
		if len(row[7])>0:			# LINE用の画像
			LineFlag = 1
			str = "\t\t\t},{\n"
			out_f.write(str)
			str = "\t\t\t\"type\" : 3, \"platform\" : \"line\", \"lang\" : \"ja\", \"imageUrl\" : \"" + row[7] + "\"\n"
			out_f.write(str)
		if len(row[8])>0:			# LINE用のボタン型選択肢
			LineFlag = 1
			str = "\t\t\t},{\n"
			out_f.write(str)
			str = "\t\t\t\"type\" : 2, \"platform\" : \"line\", \"lang\" : \"ja\", \"title\" : \"" + row[8] + "\", \"replies\" : ["
			out_f.write(str)
			if len(row[9])>0:			# LINE用のボタン型選択肢
				str = "\"" + row[9] + "\""
				out_f.write(str)
			if len(row[10])>0:			# LINE用のボタン型選択肢
				str = ",\"" + row[10] + "\""
				out_f.write(str)
			if len(row[11])>0:			# LINE用のボタン型選択肢
				str = ",\"" + row[11] + "\""
				out_f.write(str)
			str = "]\n"
			out_f.write(str)
		if len(row[12])>0:			# LINE用の画像付きボタン
			LineFlag = 1
			str = "\t\t\t},{\n"
			out_f.write(str)
			str = "\t\t\t\"type\" : 1, \"platform\" : \"line\", \"lang\" : \"ja\", \"title\" : \"" + row[12] + "\" , \"subtitle\" : \"" + row[13] + "\" , \"imageUrl\" : \"" + row[14] + "\" , \"buttons\" : ["
			out_f.write(str)
			if len(row[15])>0:			# LINE用のボタン型選択肢
				str = "{\"text\" : " + "\"" + row[15] + "\""
				out_f.write(str)
				if len(row[16])>0:			# LINE用のボタン型選択肢
					str = ",\"postback\" : " + "\"" + row[16] + "\""
					out_f.write(str)
				str = "}"
				out_f.write(str)
			if len(row[17])>0:				# LINE用のボタン型選択肢
				str = ",{\"text\" : " + "\"" + row[17] + "\""
				out_f.write(str)
				if len(row[18])>0:			# LINE用のボタン型選択肢
					str = ",\"postback\" : " + "\"" + row[18] + "\""
					out_f.write(str)
				str = "}"
				out_f.write(str)
			if len(row[19])>0:				# LINE用のボタン型選択肢
				str = ",{\"text\" : " + "\"" + row[19] + "\""
				out_f.write(str)
				if len(row[20])>0:			# LINE用のボタン型選択肢
					str = ",\"postback\" : " + "\"" + row[20] + "\""
					out_f.write(str)
				str = "}"
				out_f.write(str)

			str = "]\n"
			out_f.write(str)

		if len(row[21])>0:			# LINE用のCustom
			LineFlag = 1
			str = "\t\t\t},{\n"
			out_f.write(str)
			str = "\t\t\t\"type\" : 4, \"platform\" : \"line\", \"lang\" : \"ja\", \"payload\" : { \"line\" : " + row[21] + " }"
			out_f.write(str)

		# LINE用終わり
		str = "\t\t\t}\n\t\t],\n"
		out_f.write(str)

		if LineFlag > 0:
			str = "\t\t\"defaultResponsePlatforms\" : {},\n"
		else:
			str = "\t\t\"defaultResponsePlatforms\": {\"line\": true},\n"

		out_f.write(str)
		str = "\t\t\"speech\" : []\n"
		out_f.write(str)
		str = "\t\t}\n\t],\n"
		out_f.write(str)
		str = "\t\"priority\": 500000, \"webhookUsed\" : false, \"webhookForSlotFilling\" : false, \"lastUpdate\" : 20190102, \"fallbackIntent\" : false, \"events\": []\n"
		out_f.write(str)
		str = "}\n"
		out_f.write(str)
		out_f.close

		#intentsのTraining pharaases
		out_f = open(fname2,'w',encoding="utf-8_sig")
		id = "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(4)])) + "-" +"".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(6)]))
		out_f.write('[\n\t{\n')
		str = "\t\t\"id\" : \"" + id + "\",\n"
		out_f.write(str)
		str = "\t\t\"data\" : [\n\t\t\t{\n"
		out_f.write(str)
		str = "\t\t\t\"text\" : \"" + row[1] + "\",\n"
		out_f.write(str)
		str = "\t\t\t\"userDefined\" : false\n"
		out_f.write(str)
		str = "\t\t\t}\n\t\t],\n"
		out_f.write(str)
		str = "\t\t\"isTemplate\": false, \"count\" : 0, \"updated\" : 20190102\n"
		out_f.write(str)
		str = "\t}"
		out_f.write(str)
		if len(row[3])>0:		#別の言い方
			id = "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(4)])) + "-" +"".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(6)]))
			out_f.write('\n\t,{\n')
			str = "\t\t\"id\" : \"" + id + "\",\n"
			out_f.write(str)
			str = "\t\t\"data\" : [\n\t\t\t{\n"
			out_f.write(str)
			str = "\t\t\t\"text\" : \"" + row[3] + "\",\n"
			out_f.write(str)
			str = "\t\t\t\"userDefined\" : false\n"
			out_f.write(str)
			str = "\t\t\t}\n\t\t],\n"
			out_f.write(str)
			str = "\t\t\"isTemplate\": false, \"count\" : 0, \"updated\" : 20190102\n"
			out_f.write(str)
			str = "\t}\n"
			out_f.write(str)
		if len(row[4])>0:		#別の言い方
			id = "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(4)])) + "-" +"".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(6)]))
			out_f.write('\n\t,{\n')
			str = "\t\t\"id\" : \"" + id + "\",\n"
			out_f.write(str)
			str = "\t\t\"data\" : [\n\t\t\t{\n"
			out_f.write(str)
			str = "\t\t\t\"text\" : \"" + row[4] + "\",\n"
			out_f.write(str)
			str = "\t\t\t\"userDefined\" : false\n"
			out_f.write(str)
			str = "\t\t\t}\n\t\t],\n"
			out_f.write(str)
			str = "\t\t\"isTemplate\": false, \"count\" : 0, \"updated\" : 20190102\n"
			out_f.write(str)
			str = "\t}\n"
			out_f.write(str)
		if len(row[5])>0:		#別の言い方
			id = "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(4)])) + "-" +"".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(2)])) + "-" + "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(6)]))
			out_f.write('\n\t,{\n')
			str = "\t\t\"id\" : \"" + id + "\",\n"
			out_f.write(str)
			str = "\t\t\"data\" : [\n\t\t\t{\n"
			out_f.write(str)
			str = "\t\t\t\"text\" : \"" + row[5] + "\",\n"
			out_f.write(str)
			str = "\t\t\t\"userDefined\" : false\n"
			out_f.write(str)
			str = "\t\t\t}\n\t\t],\n"
			out_f.write(str)
			str = "\t\t\"isTemplate\": false, \"count\" : 0, \"updated\" : 20190102\n"
			out_f.write(str)
			str = "\t}\n"
			out_f.write(str)		
		str = "\n]\n"
		out_f.write(str)
		out_f.close

#print "".join(map(lambda t: format(t, "02X"), [random.randrange(256) for x in range(16)]))


