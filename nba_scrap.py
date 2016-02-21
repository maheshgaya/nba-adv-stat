"""Web Scrapper for ISU Hackathon"""
"""Web Scrapper retrieves basic statistics 
of key NBA Players"""
from bs4 import BeautifulSoup 
from urllib.request import urlopen, HTTPError 

base_url = "http://espn.go.com/nba/statistics" 

stat_list = []
stat_list_two = []
stat_list_three = []
stat_list_four = []
stat_list_five = []

team_list = []
team_list_two = []
team_list_three = []
team_list_four = []
team_list_five = []

def check_open(url):
	try: 
		urlopen(url)
		print("The webpage has opened")
		return "Go"
	except HTTPError as e: 
		return None 
		print("The webpage was not opened")

def get_td_title(player_url):
	html = urlopen(player_url)
	bs_obj = BeautifulSoup(html, "lxml")
	list_of_tds = bs_obj.findAll(td)
	for td in range(len(list_of_tds)):
		print(td)


def steph_stats(base_url, stat_list):
	"""Function that gets stat of Steph"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll(("tr", {"class","oddrow"}))
	new_list = [] 
	for x in num:
		new_string = x.get_text() + " "
		print(new_string)
		stat_list.append(new_string)
	new_list.append(stat_list[21])
	return new_list

def harden_stats(base_url, stat_list):
	"""Function that gets stat of Harden"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll(("tr", {"class","oddrow"}))
	new_list = [] 
	for x in num:
		new_string = x.get_text() + " "
		stat_list_two.append(new_string)
	new_list.append(stat_list[21])
	return new_list

def durant_stats(base_url, stat_list):
	"""Function that gets stat of Durant"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll(("tr", {"class","oddrow"}))
	new_list = [] 
	for x in num:
		new_string = x.get_text() + " "
		stat_list_three.append(new_string)
	new_list.append(stat_list_three[25])
	return new_list

def cousins_stats(base_url, stat_list):
	"""Function that gets stat of Cousins"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll(("tr", {"class","oddrow"}))
	new_list = [] 
	for x in num:
		new_string = x.get_text() + " "
		#print(new_string)
		stat_list_four.append(new_string)
	new_list.append(stat_list_four[19])
	return new_list

def lebron_stats(base_url, stat_list):
	"""Function that gets stat of Lebron"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll(("tr", {"class","oddrow"}))
	new_list = [] 
	for x in num:
		new_string = x.get_text() + " "
		#print(new_string)
		stat_list_five.append(new_string)
	new_list.append(stat_list_five[33])
	return new_list

def gs_team_stat(base_url, team_list):
	"""Function that computes GS stat"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll("tr", {"class": "oddrow team-46-9"})
	new_list = []
	for x in num:
		new_string = x.get_text() + " "
		print(new_string)
		team_list.append(new_string)
	new_list.append(team_list[0])
	return new_list

def hou_team_stat(base_url, team_list):
	"""Function that computes Houston stat"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll("tr", {"class": "evenrow team-46-10"})
	new_list = []
	for x in num:
		new_string = x.get_text() + " "
		print(new_string)
		team_list.append(new_string)
	new_list.append(team_list[0])
	return new_list

def okc_team_stat(base_url, team_list):
	"""Function that computes Thunder stat"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll("tr", {"class": "evenrow team-46-25"})
	new_list = []
	for x in num:
		new_string = x.get_text() + " "
		print(new_string)
		team_list_three.append(new_string)
	new_list.append(team_list_three[0])
	return new_list

def sac_team_stat(base_url, team_list):
	"""Function that computes Sacramento stat"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll("tr", {"class": "oddrow team-46-23"})
	new_list = []
	for x in num:
		new_string = x.get_text() + " "
		print(new_string)
		team_list_four.append(new_string)
	new_list.append(team_list_four[0])
	return new_list

def cle_team_stat(base_url, team_list):
	"""Function that computes Cleavland stat"""
	html = urlopen(base_url)
	bs_obj = BeautifulSoup(html, "lxml")
	num = bs_obj.findAll("tr", {"class": "evenrow team-46-5"})
	new_list = []
	for x in num:
		new_string = x.get_text() + " "
		print(new_string)
		team_list_five.append(new_string)
	new_list.append(team_list_five[0])
	return new_list

def steph_create(data):
	"""A function that computes data for Stephen Curry"""

	# Splits strings into respective variables
	split_data = data[0]
	year = split_data[1:7]
	team = split_data[7:9]

	fg_made = split_data[9:12]
	fg_attempted = split_data[13:16+1]
	fg_pec = split_data[16+1:20+1]

	three_made = split_data[20+1:23+1]
	three_attempted = split_data[24+1:27+1]
	three_pec = split_data[27+1:31+1]

	ft_made = split_data[31+1:34+1]
	ft_attempted = split_data[35+1:38+1]
	ft_pec = split_data[38+1:42+1]

	off_re = split_data[42+1:44+1]
	def_re = split_data[44+1:47+1]
	reb = split_data[47+1:50+1]
	ast = split_data[50+1:53+1]
	blk = split_data[53+1:55+1]
	stl = split_data[55+1:58+1]

	personal_f = split_data[58+1:61+1]
	turnover = split_data[61+1:64+1]
	points = split_data[64+1:68+1]

	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(off_re)
	print(def_re)
	print(reb)
	print(ast)
	print(blk)
	print(stl)
	print(personal_f)
	print(turnover)
	print(points)

	# Writes the variables to the text file
	filename = open("steph.txt", "w+")
	for x in range(1):
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(off_re +"\n") 
		filename.write(def_re +"\n") 
		filename.write(reb +"\n") 
		filename.write(ast +"\n") 
		filename.write(blk +"\n") 
		filename.write(stl +"\n") 
		filename.write(personal_f +"\n") 
		filename.write(turnover +"\n") 
		filename.write(points +"\n") 
		filename.write("33.7" + "\n")
		filename.write("32.21" + '\n')  		
		filename.write("51" + "\n")

def harden_create(data):
	"""A function that computes data for James Harden"""

	# Splits strings into respective variables
	split_data = data[0]
	year = split_data[1:7]
	team = split_data[7:9]
	
	fg_made = split_data[10:13]
	fg_attempted = split_data[14:18]
	fg_pec = split_data[18:22]
	
	three_made = split_data[22:25]
	three_attempted = split_data[26:29]
	three_pec = split_data[29:33]
	
	ft_made = split_data[33:36]
	ft_attempted = split_data[37:40]
	ft_pec = split_data[40:44]
	
	off_re = split_data[44:46]
	def_re = split_data[46:49]
	reb = split_data[49:52]
	ast = split_data[52:55]
	blk = split_data[55:57]
	stl = split_data[57:59]
	personal_f = split_data[59:62]
	turnover = split_data[62:65]
	points = split_data[65:70]

	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(off_re)
	print(def_re)
	print(reb)
	print(ast)
	print(blk)
	print(stl)
	print(personal_f)
	print(turnover)
	print(points)

	# Writes the variables to the text file
	filename = open("harden.txt", "w+")
	for x in range(1):
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(off_re +"\n") 
		filename.write(def_re +"\n") 
		filename.write(reb +"\n") 
		filename.write(ast +"\n") 
		filename.write(blk +"\n") 
		filename.write(stl +"\n") 
		filename.write(personal_f +"\n") 
		filename.write(turnover +"\n") 
		filename.write(points +"\n") 	
		filename.write("37.3" + "\n")  
		filename.write("25.35" + "\n")
		filename.write("56" + "\n")


def durant_create(data):
	"""A function that computes data for Kevin Durant"""

	# Splits strings into respective variables
	split_data = data[0]
	year = split_data[1:7]
	team = split_data[7:9]
	
	fg_made = split_data[10:13]
	fg_attempted = split_data[14:17]
	fg_pec = split_data[17:21]
	
	three_made = split_data[21:24]
	three_attempted = split_data[25:28]
	three_pec = split_data[28:32]
	
	ft_made = split_data[32:35]
	ft_attempted = split_data[36:39]
	ft_pec = split_data[39:43]
	
	off_re = split_data[43:45]
	def_re = split_data[45:48]
	reb = split_data[48:51]
	ast = split_data[51:54]
	blk = split_data[54:56]
	stl = split_data[56:58]
	personal_f = split_data[58:60]
	turnover = split_data[60:63]
	points = split_data[63:69]

	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(off_re)
	print(def_re)
	print(reb)
	print(ast)
	print(blk)
	print(stl)
	print(personal_f)
	print(turnover)
	print(points)

	# Writes the variables to the text file
	filename = open("durant.txt", "w+")
	for x in range(1):
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(off_re +"\n") 
		filename.write(def_re +"\n") 
		filename.write(reb +"\n") 
		filename.write(ast +"\n") 
		filename.write(blk +"\n") 
		filename.write(stl +"\n") 
		filename.write(personal_f +"\n") 
		filename.write(turnover +"\n") 
		filename.write(points +"\n") 	
		filename.write("36.1" + "\n") 
		filename.write("28.18" +"\n") 
		filename.write("48"+ "\n")


def cousins_create(data):
	"""A function that computes data for Demarcus Cousins"""

	# Splits strings into respective variables
	split_data = data[0]
	year = split_data[1:7]
	team = split_data[7:9]
	
	fg_made = split_data[10:13]
	fg_attempted = split_data[14:17]
	fg_pec = split_data[17:21]
	
	three_made = split_data[21:23]
	three_attempted = split_data[24:27]
	three_pec = split_data[27:31]
	
	ft_made = split_data[31:34]
	ft_attempted = split_data[35:38]
	ft_pec = split_data[38:42]
	
	off_re = split_data[42:45]
	def_re = split_data[45:48]
	reb = split_data[48:51]
	ast = split_data[51:54]
	blk = split_data[54:56]
	stl = split_data[56:58]
	personal_f = split_data[58:61]
	turnover = split_data[61:64]
	points = split_data[64:69]

	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(off_re)
	print(def_re)
	print(reb)
	print(ast)
	print(blk)
	print(stl)
	print(personal_f)
	print(turnover)
	print(points)

	# Writes the variables to the text file
	filename = open("cousins.txt", "w+")
	for x in range(1):
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(off_re +"\n") 
		filename.write(def_re +"\n") 
		filename.write(reb +"\n") 
		filename.write(ast +"\n") 
		filename.write(blk +"\n") 
		filename.write(stl +"\n") 
		filename.write(personal_f +"\n") 
		filename.write(turnover +"\n") 
		filename.write(points +"\n") 
		filename.write("34.6" + "\n")  
		filename.write("23.56" + "\n")		
		filename.write("45" + "\n")



def lebron_create(data):
	"""A function that computes data for Lebron James"""

	# Splits strings into respective variables
	split_data = data[0]
	year = split_data[1:7]
	team = split_data[7:9]
	
	fg_made = split_data[10:13]
	fg_attempted = split_data[14:17]
	fg_pec = split_data[17:21]
	
	three_made = split_data[21:23]
	three_attempted = split_data[24:27]
	three_pec = split_data[27:31]
	
	ft_made = split_data[31:34]
	ft_attempted = split_data[35:38]
	ft_pec = split_data[38:42]
	
	off_re = split_data[42:44]
	def_re = split_data[44:47]
	reb = split_data[47:50]
	ast = split_data[50:53]
	blk = split_data[53:55]
	stl = split_data[55:57]
	personal_f = split_data[57:60]
	turnover = split_data[60:63]
	points = split_data[63:68]

	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(off_re)
	print(def_re)
	print(reb)
	print(ast)
	print(blk)
	print(stl)
	print(personal_f)
	print(turnover)
	print(points)

	# Writes the variables to the text file
	filename = open("lebron.txt", "w+")
	for x in range(1):
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(off_re +"\n") 
		filename.write(def_re +"\n") 
		filename.write(reb +"\n") 
		filename.write(ast +"\n") 
		filename.write(blk +"\n") 
		filename.write(stl +"\n") 
		filename.write(personal_f +"\n") 
		filename.write(turnover +"\n") 
		filename.write(points +"\n") 
		filename.write("35.8" + "\n")  
		filename.write("26.99" +"\n")	
		filename.write("52"+"\n")

def gs_create(data):
	"""A function that computes data for Golden State"""

	# Splits strings into respective variables
	
	split_data = data[0]
	team = split_data[2-1:14-1]
	points = split_data[14-1:18-1]

	fg_made = split_data[18-1:22-1]
	fg_attempted = split_data[22-1:26-1]
	fg_pec = split_data[26-1:30-1]
	
	three_made = split_data[30-1:33-1]
	three_attempted = split_data[33-1:36-1]
	three_pec = split_data[36-1:40-1]
	
	ft_made = split_data[40-1:43-1]
	ft_attempted = split_data[43-1:47-1]
	ft_pec = split_data[47-1:51-1]
	
	pps = split_data[51-1:55-1]
	afg = split_data[55-1:59-1]
	
	print(team)
	print(points)
	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(pps)
	print(afg)
	

	# Writes the variables to the text file
	filename = open("golden_state.txt", "w+")
	for x in range(1):
		filename.write(points +"\n") 
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(pps +"\n") 
		filename.write(afg +"\n") 
		filename.write("48" + "\n") 
		filename.write("5" + "\n") 	
		filename.write("802" + "\n")	


def houston_create(data):
	"""A function that computes data for Houston"""

	# Splits strings into respective variables
	
	split_data = data[0]
	team = split_data[1:8]
	points = split_data[8:12]

	fg_made = split_data[12:16]
	fg_attempted = split_data[16:20]
	fg_pec = split_data[20:24]
	
	three_made = split_data[24:27]
	three_attempted = split_data[27:31]
	three_pec = split_data[31:35]
	
	ft_made = split_data[35:39]
	ft_attempted = split_data[39:43]
	ft_pec = split_data[43:47]
	
	pps = split_data[47:51]
	afg = split_data[51:55]
	
	print(team)
	print(points)
	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(pps)
	print(afg)
	

	# Writes the variables to the text file
	filename = open("houston.txt", "w+")
	for x in range(1):
		filename.write(points +"\n") 
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(pps +"\n") 
		filename.write(afg +"\n") 	
		filename.write("28" + "\n") 
		filename.write("28" + "\n") 
		filename.write("872" + "\n")	
	

def okc_create(data):
	"""A function that computes data for Thunder"""

	# Splits strings into respective variables
	split_data = data[0]
	team = split_data[1:14]
	points = split_data[8+6:12+6]

	fg_made = split_data[12+6:16+6]
	fg_attempted = split_data[16+6:20+6]
	fg_pec = split_data[20+6:24+6]
	
	three_made = split_data[24+6:27+6]
	three_attempted = split_data[27+6:31+6]
	three_pec = split_data[31+6:35+6]
	
	ft_made = split_data[35+6:39+6]
	ft_attempted = split_data[39+6:43+6]
	ft_pec = split_data[43+6:47+6]
	
	pps = split_data[47+6:51+6]
	afg = split_data[51+6:55+6]
	
	print(team)
	print(points)
	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(pps)
	print(afg)
	

	# Writes the variables to the text file
	filename = open("thunder.txt", "w+")
	for x in range(1):
		filename.write(points +"\n") 
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(pps +"\n") 
		filename.write(afg +"\n") 	
		filename.write("40" + "\n") 
		filename.write("15" + "\n") 
		filename.write("835" + "\n")


def sac_create(data):
	"""A function that computes data for Houston"""

	# Splits strings into respective variables
	
	split_data = data[0]
	team = split_data[1:11]
	points = split_data[8+3:12+3]

	fg_made = split_data[12+3:16+3]
	fg_attempted = split_data[16+3:20+3]
	fg_pec = split_data[20+3:24+3]
	
	three_made = split_data[24+3:27+3]
	three_attempted = split_data[27+3:31+3]
	three_pec = split_data[31+3:35+3]
	
	ft_made = split_data[35+3:39+3]
	ft_attempted = split_data[39+3:43+3]
	ft_pec = split_data[43+3:47+3]
	
	pps = split_data[47+3:51+3]
	afg = split_data[51+3:55+3]
	
	print(team)
	print(points)
	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(pps)
	print(afg)
	

	# Writes the variables to the text file
	filename = open("sacramento.txt", "w+")
	for x in range(1):
		filename.write(points +"\n") 
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(pps +"\n") 
		filename.write(afg +"\n") 
		filename.write("23" + "\n") 
		filename.write("31" + "\n") 	
		filename.write("862" +"\n")	



def cle_create(data):
	"""A function that computes data for Cleavland"""

	# Splits strings into respective variables
	
	split_data = data[0]
	team = split_data[2:11]
	points = split_data[14-3:18-3]

	fg_made = split_data[18-3:22-3]
	fg_attempted = split_data[22-3:26-3]
	fg_pec = split_data[26-3:30-3]
	
	three_made = split_data[30-3:33-3]
	three_attempted = split_data[33-3:36-2]
	three_pec = split_data[36-2:40-2]
	
	ft_made = split_data[40-2:43-2]
	ft_attempted = split_data[43-2:47-2]
	ft_pec = split_data[47-2:51-2]
	
	pps = split_data[51-2:55-2]
	afg = split_data[55-2:59-2]
	
	print(team)
	print(points)
	print(fg_made)
	print(fg_attempted)
	print(fg_pec)
	print(three_made)
	print(three_attempted)
	print(three_pec)
	print(ft_made)
	print(ft_attempted)
	print(ft_pec)
	print(pps)
	print(afg)
	

	# Writes the variables to the text file
	filename = open("cleavland.txt", "w+")
	for x in range(1):
		filename.write(points +"\n") 
		filename.write(fg_made +"\n") 
		filename.write(fg_attempted +"\n") 
		filename.write(fg_pec +"\n") 
		filename.write(three_made+"\n") 
		filename.write(three_attempted +"\n") 
		filename.write(three_pec +"\n") 
		filename.write(ft_made+"\n") 
		filename.write(ft_attempted +"\n") 
		filename.write(ft_pec +"\n") 
		filename.write(pps +"\n") 
		filename.write(afg +"\n")
		filename.write("39" + "\n") 
		filename.write("14" + "\n")
		filename.write("674") 	



def main():
	"""Main function"""
	# Checks if the webpage will open
	check_open(base_url)

	team_url = "http://espn.go.com/nba/statistics/team/_/stat/offense"
	# For Steph
	steph = "http://espn.go.com/nba/player/stats/_/id/3975/stephen-curry"
	s_data = steph_stats(steph, stat_list)
	steph_data = []
	steph_data.append(s_data[0])
	print(steph_data)
	steph_create(steph_data)

	# For Harden
	harden = "http://espn.go.com/nba/player/stats/_/id/3992/james-harden" 
	h_data = harden_stats(harden, stat_list_two)
	harden_data = []
	harden_data.append(h_data[0])
	print(harden_data)
	harden_create(harden_data)

	# For Durant 
	durant = "http://espn.go.com/nba/player/stats/_/id/3202/kevin-durant"
	dur_data = durant_stats(durant, stat_list_three)
	durant_data = []
	durant_data.append(dur_data[0])
	print(durant_data)
	durant_create(durant_data)

	# For Cousins 
	cousins = "http://espn.go.com/nba/player/stats/_/id/4258/demarcus-cousins"
	c_data = cousins_stats(cousins, stat_list_four)
	cousins_data = []
	cousins_data.append(c_data[0])
	print(cousins_data)
	cousins_create(cousins_data) 

	# For Lebron 
	lebron = "http://espn.go.com/nba/player/stats/_/id/1966/lebron-james"
	leb_data = lebron_stats(lebron, stat_list_five)
	lebron_data = []
	lebron_data.append(leb_data[0])
	print(lebron_data)
	lebron_create(lebron_data)

	# for Golden State 
	g_data = gs_team_stat(team_url, team_list)
	gs_data = []
	gs_data.append(g_data[0]) 
	print(gs_data)
	gs_create(gs_data)

	# for Houston
	h_data = hou_team_stat(team_url, team_list_two)
	houston_data = []
	houston_data.append(h_data[0]) 
	print(houston_data)
	houston_create(houston_data)

	# for OKC
	o_data = okc_team_stat(team_url, team_list_three)
	okc_data = []
	okc_data.append(o_data[0]) 
	print(okc_data)
	okc_create(okc_data)

	# for Sac
	sa_data = sac_team_stat(team_url, team_list_four)
	sac_data = []
	sac_data.append(sa_data[0]) 
	print(sac_data)
	sac_create(sac_data)

	# for Cleavland
	cl_data = cle_team_stat(team_url, team_list_five)
	cle_data = []
	cle_data.append(cl_data[0]) 
	print(cle_data)
	cle_create(cle_data)



if __name__ == "__main__":
	main()
	

	

