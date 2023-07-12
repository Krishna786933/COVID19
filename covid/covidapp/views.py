from django.shortcuts import render
import json

import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
	"X-RapidAPI-Key": "48c89271a4msh36e794f3f7704a1p14ad5cjsn60eb07b4b08c",
	"X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()



def hello(request):
    mylist = []
    for i in range(0,200):
        mylist.append(response['countries_stat'][i]['country_name'])
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        for x in range(0,210):
            if selectedcountry==response['countries_stat'][x]['country_name']:
                cases = response['countries_stat'][x]['cases']
                deaths = response['countries_stat'][x]['deaths']
                new_deaths = response['countries_stat'][x]['new_deaths']
                new_cases = response['countries_stat'][x]['new_cases']
                total_recovered = response['countries_stat'][x]['total_recovered']
                active_cases = response['countries_stat'][x]['active_cases']
                total_cases_per_1m_population = response['countries_stat'][x]['total_cases_per_1m_population']
                total_tests = response['countries_stat'][x]['total_tests']
                deaths_per_1m_population = response['countries_stat'][x]['deaths_per_1m_population']

        context = {'mylist':mylist,'selectedcountry':selectedcountry,'new':new_cases,'active':active_cases,'newDeaths':new_deaths,'recovered': total_recovered,'total':cases,'deaths':deaths,'t_c_1m_p':total_cases_per_1m_population,'total_tests':total_tests,'t_d_1m_p':deaths_per_1m_population}
        return render(request,'helloworld.html',context)
        



               


    
    return render(request,'helloworld.html',{'mylist':mylist})
    
    


# 'country_name': 'USA', 'cases': '82,649,779', 'deaths': '1,018,316', 'region': '', 'total_recovered': '80,434,925', 'new_deaths': '0', 'new_cases': '0', 'serious_critical': '1,465', 'active_cases': '1,196,538', 'total_cases_per_1m_population': '247,080', 'deaths_per_1m_population': '3,044', 'total_tests': '1,000,275,726', 'tests_per_1m_population': '2,990,303'}



def base(request):
    return render(request,"base.html")