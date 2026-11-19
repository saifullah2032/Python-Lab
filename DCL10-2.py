name = "Ishan"
age = 72
speed = 2.4
print(f"{name} whose age is {age} walks at a speed of {speed} km/hr.")
stmt = name + " whose age is " + \
    str(age)+" walks at a speed of "+str(speed)+" km/hr"
print(stmt)
team1 = input("Enter Team1: ")
team2 = input("Enter Team2: ")
rivalry = input("Type of Rivalry: ")
score = int(input("Enter the Score: "))
run_rate = float(input("Enter the run rate: "))
print(f"{team1} won against {team2} who is {rivalry} rival by scoring {score} runrate of {run_rate}")
string = "{} won against {} who is {} rival by scoring {} run rate of {}".format(
    team1, team2, rivalry, score, run_rate)
print(string)
