//showheading(): show heading for statistics table
function showheading(){
	document.write("<thead>");
	document.write("<tr>");
	document.write("<th title='Field Goals Made'>FGM</th>");
	document.write("<th title='Field Goals Attempted'>FGA</th>");
	document.write("<th title='Field Goals Percentage'>FG%</th>");
	document.write("<th title='3-Point Shots Made'>3PM</th>");
	document.write("<th title='3-Point Shots Attempted'>3PA</th>");
	document.write("<th title='3-Point Shots Percentage'>3P%</th>");
	document.write("<th title='Free Throws Made'>FTM</th>");
	document.write("<th title='Free Throws Attempted'>FTA</th>");
	document.write("<th title='Free Throw Percentage'>FT%</th>");
	document.write("<th title='Offensive Rebounds'>ORB</th>");
	document.write("<th title='Defensive Rebounds'>DRB</th>");
	document.write("<th title='Total Rebounds'>TRB</th>");
	document.write("<th title='Assists'>AST</th>");
	document.write("<th title='Blocks'>BLK</th>");
	document.write("<th title='Steals'>STL</th>");
	document.write("<th title='Personal Fouls'>PF</th>");
	document.write("<th title='Turnovers'>TOV</th>");
	document.write("<th title='Points'>PTS</th>");
	document.write("<th title='Minutes Played'>MP</th>");
	document.write("<th title='Player Efficiency Rating'>PER</th>");
	document.write("<th title='Games Played'>GP</th>");
	document.write("</tr>");
	document.write("</thead>");

}

//showAdvHeading(): show heading for advanced statistics table
function showAdvHeading(){
	document.write("<thead>");
	document.write("<tr>");
	document.write("<th title='True Shooting Percentage: A statistic used to gauge shooting efficiency that takes into consideration points scored from three pointers, field goals and free-throws to get a measure of points scored each shooting attempt.'>TS%</th>");
	document.write("<th title='Effecting Field Goal Percentage: Adjusts for the fact that a 3-point FG is worth one more than a 2-point FG'>eFG%</th>");
	document.write("<th title='Turnover Percentage: An estimate of turnovers per 100 plays.'>TOV%</th>");
	document.write("<th title='Assists to Turnover Ratio'>AST/TOV</th>");
	document.write("<th title='Free Throw Rate: Ratio of free throws to total shots'>FTr</th>");
	document.write("<th title='3-Point Rate: Ratio of 3-point shots to total shots'>3Pr</th>");
	document.write("<th title='2-Point Rate: Ratio of 2-point shots to total shots'>2Pr</th>");
	document.write("<th title='Assists Percentage'>AST%</th>");
	document.write("<th title='Usage Percentage'>USG%</th>");
	document.write("</tr>");
	document.write("</thead>");
}

function showTeamHeading(){
	document.write("<thead>");
	document.write("<tr>");
	document.write("<th title='Points'>PTS</th>");
	document.write("<th title='Field Goals Made'>FGM</th>");
	document.write("<th title='Field Goals Attempted'>FGA</th>");
	document.write("<th title='Field Goals Percentage'>FG%</th>");
	document.write("<th title='3-Point Shots Made'>3PM</th>");
	document.write("<th title='3-Point Shots Attempted'>3PA</th>");
	document.write("<th title='3-Point Shots Percentage'>3P%</th>");
	document.write("<th title='Free Throws Made'>FTM</th>");
	document.write("<th title='Free Throws Attempted'>FTA</th>");
	document.write("<th title='Free Throw Percentage'>FT%</th>");
	document.write("<th title='Points Per Shot'>PPS</th>");
	document.write("<th title='Adjusted Field Goal Percentage'>AFG%</th>");
	document.write("<th title='Wins'>WINS</th>");
	document.write("<th title='Losses'>LOSSES</th>");
	document.write("<th title='Turnovers'>TOV</th>");
	document.write("</tr>");
	document.write("</thead>");
}


$(function(){
	$(document).tooltip();
});
