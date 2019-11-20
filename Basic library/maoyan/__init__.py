import get_one_page
import parse_one_page


if __name__ == '__main__':
    url='https://maoyan.com/cinemas'
    html=get_one_page.get_one_page(url)
    print(html)
    parse_one_page.parse_one_page(html)
      #  print(item)
    #print(html)


