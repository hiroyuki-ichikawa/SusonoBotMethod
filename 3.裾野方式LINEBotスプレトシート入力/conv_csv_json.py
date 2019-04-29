# coding:utf-8
import csv
import random
import sys

args = sys.argv

filename = './' + args[1]


with open(filename, 'r') as f:
	reader = csv.reader(f)
	header = next(reader)  # 読み込み

	for row in reader:
		print row[1]       # intentsのファイル名、名前
		fname  = "./intents/" + row[1] + ".json"
		fname2 = "./intents/" + row[1] + "_usersays_ja.json"
		print fname

		# intentsファイル
		out_f = open(fname,'w')
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
		str = "\t\t\t{\n"
		out_f.write(str)
		str = "\t\t\t\"type\" : 0, \"lang\" : \"ja\", \"speech\" : \"" + row[2] + "\"\n"
		out_f.write(str)
		str = "\t\t\t},{\n"
		out_f.write(str)
		str = "\t\t\t\"type\" : 0, \"lang\" : \"ja\", \"speech\" : []\n"
		out_f.write(str)
		str = "\t\t\t}\n\t\t],\n"
		out_f.write(str)
		str = "\t\t\"defaultResponsePlatforms\" : {},\n"
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
		out_f = open(fname2,'w')
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


