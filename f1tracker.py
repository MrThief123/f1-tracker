from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Extract the current date
year = str(current_datetime.year)


from requests_html import HTML, HTMLSession

# Create an HTML session
session = HTMLSession()


# Fetch the web page
driverresponse = session.get('https://www.formula1.com/en/results.html/'+year+'/drivers.html')

# Check if the request was successful
if driverresponse.status_code == 200:
    # Parse the HTML content
    htmldriver = HTML(html=driverresponse.text)
else:
    print(f"Failed to retrieve the page. Status code: {driverresponse.status_code}")


stats = htmldriver.find('tbody tr')

drivers = []
points = []


print('\n\nDriver Standings')
for stat in stats:
    position = stat.find('td')[1].text
    driver = stat.find('td')[2].text
    car = stat.find('td')[4].text

    if len(car.split()) > 2:
        car= ' '.join(stat.find('td')[4].text.split()[:2]) 

    point = stat.find('td')[5].text
    code = driver.split()[-1]
    name = ' '.join(driver.split()[:-1])
    drivers.append(code)
    points.append(point)
    print(f'{position+".":<4.3s}{code}  {name:16.16s}  {car:<20.20}   {point}')



#constrcutors 

Constrcutor_response = session.get('https://www.formula1.com/en/results.html/'+year+'/team.html')

Constructor_html = HTML(html=Constrcutor_response.text)

stats = Constructor_html.find('tbody tr')

print('\n\n\n\nConstructors Standings')
for stat in stats:
    position = stat.find('td')[1].text
    team = stat.find('td')[2].text
    point = stat.find('td')[3].text
    print(f'{position+".":<4.2}{team:<32.31}{point}')

print('\n\n\n\n')
# recent race
print('Race Stats')

recent_race_response = session.get('https://www.formula1.com/en/results.html/'+year+'/races.html')
recent_html =  HTML(html=recent_race_response.text)
winner_stats = recent_html.find('tbody tr')

fast_response = session.get('https://www.formula1.com/en/results.html/'+year+'/fastest-laps.html')
fast_html =  HTML(html=fast_response.text)
fast_stats = fast_html.find('tbody tr')


print(f'{"Grand Prix":<20.20s}{"Winner":<20.20s}{"Fastest Lap":<12.12}{"Time"}')
for num, stat in enumerate(winner_stats):
    gp = stat.find('td')[1].text
    winner = stat.find('td')[3].text
    name = ' '.join(winner.split()[:-1])
    fast_driver = fast_stats[num].find('td')[2].text.split()[-1]
    fast_time = fast_stats[num].find('td')[4].text
    print(f'{gp:<20.20s}{name:<20.20}{fast_driver:<8.8}{fast_time}')
    
    


