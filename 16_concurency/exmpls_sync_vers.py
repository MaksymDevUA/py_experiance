import requests
import time


session = requests.Session() #The current session
print(session) #Represented as object

def download_site(url, session): #take session.get website and output some params
    with session.get(url) as response: #get request to url in seesion and capture in response(send a request to the url using the session object, and while you're at it, capture the response and call it response.") Can use "response" to access the content of the webpage you requested
        print(f"Read {len(response.content)} from {url}")
        print(response)
        print(response.content)
def download_all_sites(sites): #open each site and perform download_site funct
    with requests.Session() as session: #assign current session to session var
        for url in sites:
            download_site(url, session)


if __name__ == "__main__": #Python idiom used to check if the current script is being run as the main program.
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ]
start_time = time.time() #current time
download_all_sites(sites)
duration = time.time() - start_time
print(f"Downloaded {len(sites)} in {duration} seconds")
