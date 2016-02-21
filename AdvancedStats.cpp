#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

double calcTS(double, double, double);
double calcEFG(double, double, double);
double calcTOV(double, double, double);
double calcAT(double, double);
double calcFTR(double, double);
double calcTHPR(double, double);
double calcTWPR(double);
double calcMP(double, double);
double calcTMP(double);
double calcAST(double, double, double, double, double);
double calcUSG(double, double, double, double, double, double, double, double);


int main()
{
	int x; //used for continuing the do while loop

	//declare ints for keeping track of array index and size
	int statsSize = 21;
	//declare array to hold the player statistics 
	double stats [statsSize];

	int teamSize = 14;
	//declare array to hold team stats
	double team [teamSize];
	
	do{	
		int statsIndex = 0; //initialized here for the case we do multiple players
		int teamIndex = 0;

		for (int i = 0; i < 2; i++)
		{
		
			//create input file and string for the filename
			ifstream inputFile;
			string inputFilename;
			//string for reading through the input file
			string word;

			if(i == 0)
			{
				//prompt the user for the name of a file to input
				cout << "Give the name of the player's file you want to input: " << endl;
				cin >> inputFilename;
				inputFile.open(inputFilename);
			}
			else
			{
				//prompt the user for the name of a file to input
				cout << "Give the name of the corresponding team file: " << endl;
				cin >> inputFilename;
				inputFile.open(inputFilename);
			}

			//check if the file opens and prompts user until it opens
			if(!inputFile)
			{
				do
				{
					cout << "Error opening file. Please give a correct file name: " << endl;
					cin >> inputFilename;
					inputFile.open(inputFilename);
				}while(!inputFile);
			}
			cin.ignore(); //eats newline left over

			//Using getline() to read one line at a time.
		  	string line;
		  	while (getline(inputFile, line)) 
		  	{
		    	if (line.empty()) continue;

		    	// Using istringstream to read the line into doubles
		    	istringstream iss(line);
		    	double num = 0.0, next = 0.0;
		    	while (iss >> next) num = next;
		    	//load the values into the stats array and update the index
		    	if(i == 0)
		    	{
		    		stats[statsIndex] = next;
		    		statsIndex++;
		    	}
		    	else
		    	{
		    		team[teamIndex] = next;
		    		teamIndex++;
		    	}
	 		}

		inputFile.close();
		}
		/*
	 	//testing outputing and manipulating the stats array
	 	for (int i = 0; i < statsSize; i++)
	 	{
	 		cout << stats[i] << endl;
	 	}

	 	double test1;
	 	test1 = stats[0] + stats[1];
	 	cout << test1 << endl << endl;
	 	
	 	//testing outputing and manipulating the team array
	 	for (int i = 0; i < teamSize; i++)
	 	{
	 		cout << team[i] << endl;
	 	}

	 	double test2;
	 	test2 = team[0] + team[1];
	 	cout << test2 << endl;
	 	*/
	 	
	 	double ts;
	 	ts = calcTS(stats[17], stats[1], stats[7]);

	 	double eFG;
	 	eFG = calcEFG(stats[0], stats[3], stats[1]);

	 	double tov;
	 	tov = calcTOV(stats[16], stats[1], stats[7]);

	 	double astTov;
	 	astTov = calcAT(stats[12], stats[16]);

	 	double ftr;
	 	ftr = calcFTR(stats[7], stats[1]);

	 	double thpr;
	 	thpr = calcTHPR(stats[4], stats[1]);

	 	double twpr;
	 	twpr = calcTWPR(thpr);

	 	double mp;
	 	mp = calcMP(stats[18], stats[20]);

	 	double teamMP;
	 	teamMP = calcTMP(stats[20]);

	 	double ast;
	 	ast = calcAST(stats[12], mp, teamMP, team[1], stats[0]);

	 	double usg;
	 	usg = calcUSG(stats[1], stats[7], stats[16], teamMP, mp, team[2], team[8], team[14]);

		//create output file and string for filename
		ofstream outputFile;
		string outputFilename;

		//prompt the user for the name of an output file
		cout << "Give the name of a file to output the results to: " << endl;
		getline(cin, outputFilename);
		outputFile.open(outputFilename);

		outputFile << ts << endl;
		outputFile << eFG << endl;
		outputFile << tov << endl;
		outputFile << astTov << endl;
		outputFile << ftr << endl;
		outputFile << thpr << endl;
		outputFile << twpr << endl;
		outputFile << mp << endl << endl;
		outputFile << teamMP << endl;
		outputFile << ast << endl;
		outputFile << usg << endl;


		outputFile.close();

		cout << "Enter 1 to do this for another file or type q to quit: " << endl;
		cin >> x;
	}while(x == 1);
	return 0;
}

/*****************************/

double calcTS(double a, double b, double c)
{
	double x;
	x = 100 * a/(2 * (b + (.44 * c)));
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcEFG(double a, double b, double c)
{
	double x;
	x = 100 * (a + (0.5 * b))/c;
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcTOV(double a, double b, double c)
{
	double x;
	x = (100 * a)/(b + (.44 * c) + a);
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcAT(double a, double b)
{
	double x;
	x = a/b;
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcFTR(double a, double b)
{
	double x;
	x = a/b;
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcTHPR(double a, double b)
{
	double x;
	x = (a/b);
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcTWPR(double a)
{
	double x;
	x = 1 - a;
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcMP(double a, double b)
{
	double x;
	x = a * b;
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcTMP(double a)
{
	double x;
	x = 5 * 48 * (a);
	return x;
}

double calcAST(double a, double b, double c, double d, double e)
{
	double x;
	x = 100 * a/(((b/(c/5))* d) - e);
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}

double calcUSG(double a, double b, double c, double d, double e, double f, double g, double h)
{
	double x;
	x = 100 * ((a + (.44 * b) + c) * (d/5))/(e * (f + (.44 * g) + h)); 
	x = floor(x * 100.00 + 0.5) / 100.00;
	return x;
}
