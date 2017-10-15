from bs4 import BeautifulSoup
import urllib.request as req


def mscore(soup):
    over = soup.select_one('#title-overview-widget')
    plot = over.select_one('.plot_summary_wrapper')
    revBar = plot.select_one('.titleReviewBar')
    revBarIt = revBar.select_one('.titleReviewBarItem')
    a = revBarIt.select('a')[0]
    return a.span.text
    
def uscore(soup):
    div = soup.select_one('.ratingValue')
    return list(div.children)[1].span.text


r = req.Request("http://www.imdb.com/title/tt3315342/?ref_=tt_rec_tt")
r.add_header('Accept','text/html')

page = req.urlopen(r)
soup = BeautifulSoup(page)


print(mscore(soup),uscore(soup))
