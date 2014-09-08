""" selected websites by categories """

CATEGORIES = [
    {
        'category': 'Retailers & General Merchandise',
        'data': [
            {
                'link': 'http://www.cspnet.com/category-news/general-merchandise',
                'select': r'/general-merchandise/'
            },
            {
                'link': 'http://www.retailgazette.co.uk/',
                'select': r'/articles/'
            },
            {
                'link': 'http://retailingtoday.com/',
                'select': r'/article/'
            },
            {
                'link': 'http://www.theretailbulletin.com/',
                'select': r'news'
            }
        ]
    },
    {
        'category': 'Dining & Nightlife',
        'data': [
            {
                'link': 'http://www.elitetraveler.com/category/finest-dining/dining-news/',
                'select': r'/dining-news/',
                'follow': '//div[@class="nav-previous"]/a',
            },
            {
                'link': 'http://www.chicagomag.com/dining-drinking/',
                'select': r'/dining-drinking/',
                'follow': '//p[@class="continued"]/a'
            },
            {
                'link': 'http://nrn.com/segments/casual-dining',
                'select': '//h3[@class="title"]/a',
                'follow': '//div[@class="button-region"]//a'
            }
        ]
    },
    {
        'category': 'News, Media & Publications',
        'data': [
            {
                'link': 'http://mashable.com/',
                'select': r'/\d+/\d+/\d+/.+'
            },
            {
                'link': 'http://www.buzzfeed.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.nytimes.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.huffingtonpost.com/',
                'select': 'all'
            },
            {
                'link': 'http://techcrunch.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Real Estate',
        'data':  [
            {
                'link': 'http://www.zillow.com/san-francisco-ca/rentals/',
                'select': r'/b/.+_ll/|/homedetails.+_zpid/',
                'follow': '//ul[@class="pagination-2012 zbti"]/li/a'
            },
            {
                'link': 'http://www.realestate.com.au/blog/news/',
                'select': r'/blog/',
                'follow': '//div[@class="wp-pagenavi"]/a'
            },
            {
                'link': 'http://www.realtor.com/apartments/Los-Angeles_CA',
                'select': r'/realestateandhomes-detail/',
                'follow': '//ol[@class="pagination pagination-pos-b"]/li/a'
            },
            {
                'link': 'http://www.worldpropertychannel.com/',
                'select': r'/north-america-residential-news/'
            }
        ]
    },
    {
        'category': 'Internet & Telecom',
        'data': [
            {
                'link': 'http://www.telecompaper.com/international/news/internet',
                'select': r'/news/',
            },
            {
                'link': 'http://www.budde.com.au/',
                'select': 'all'
            },
            {
                'link': 'http://www.telecomramblings.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.internetnews.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.internet.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Occasions & Gifts',
        'data': [
            {
                'link': 'http://www.buyagift.co.uk/',
                'select': 'all'
            },
            {
                'link': 'http://www.lovelygifts.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.harryanddavid.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Jobs & Education',
        'data': [
            {
                'link': 'http://www.indeed.com/l-Seattle,-WA-jobs.html',
                'select': 'all'
            },
            {
                'link': 'http://www.glassdoor.com/Job/jobs.htm',
                'select': 'all',
            },
            {
                'link': 'http://jobsearch.monster.com/browse/?sf=14',
                'select': r'/jobview.monster.com/',
                'follow': '//span[@class="navLinks"]//a'
            },
            {
                'link': 'http://www.huffingtonpost.com/education/',
                'select': r'utm_hp_ref=education'
            },
            {
                'link': 'http://www.theguardian.com/education',
                'select': r'/education/'
            },
        ]
    },
    {
        'category': 'Travel & Tourism',
        'data': [
            {
                'link': 'http://www.tripadvisor.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.expedia.com/?rfrr=Header.POSRedirect.www.expedia.com.vn%252FHome.htm',
                'select': 'all'
            },
            {
                'link': 'http://www.kayak.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Beauty & Personal Care',
        'data': [
            {
                'link': 'http://www.euromonitor.com/beauty-and-personal-care',
                'select': 'all'
            },
            {
                'link': 'http://www.mintel.com/category/press-centre/beauty-and-personal-care',
                'select': '//div[@class="post-title-press"]/h2/a',
                'follow': '//div[@class="pagination"]/a'
            },
            {
                'link': 'http://www.dowcorning.com/',
                'select': 'all'
            }
        ]

    },
    {
        'category': 'Vehicles',
        'data': [
            {
                'link': 'http://www.gm.com/vehicles/browseByType.html',
                'select': 'all'
            },
            {
                'link': 'http://www.usedcars.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.autotrader.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Law & Government',
        'data': [
            {
                'link': 'http://www.hg.org/',
                'select': 'all'
            },
            {
                'link': 'http://www.theguardian.com/law',
                'select': r'/law/'
            },
            {
                'link': 'http://www.bloomberg.com/news/law/',
                'select': r'/news/',
                'follow': '//ul[@section_name="more_LAW"]//li//a'
            },
            {
                'link': 'http://www.law.com/',
                'select': r'/sites/articles/',
            }
        ]
    },
    {
        'category': 'Food & Groceries',
        'data': [
            {
                'link': 'http://www.foodbeast.com/',
                'select': 'all',
            },
            {
                'link': 'http://www.independent.co.uk/life-style/food-and-drink/news/',
                'select': r'/food-and-drink/',
                'follow': '/div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.foodsafetynews.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Apparel',
        'data': [
            {
                'link': 'http://www.americanapparel.net/',
                'select': 'all'
            },
            {
                'link': 'http://www.alternativeapparel.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.zappos.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Finance',
        'data': [
            {
                'link': 'http://www.efinancialnews.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.reuters.com/finance',
                'select': r'/article/'
            },
            {
                'link': 'http://www.bloomberg.com/news/finance/',
                'select': r'/news/'
            }
        ]
    },
    {
        'category': 'Arts & Entertainment',
        'data': [
            {
                'link': 'http://www.bbc.com/news/entertainment_and_arts/',
                'select': r'/news/entertainment-arts'
            },
            {
                'link': 'http://www.telegraph.co.uk/culture/',
                'select': r'/culture/'
            },
            {
                'link': 'http://www.independent.co.uk/arts-entertainment/',
                'select': r'/arts-entertainment'
            }
        ]
    },
    {
        'category': 'Family & Community',
        'data': [
            {
                'link': 'http://www.theguardian.com/lifeandstyle/family',
                'select': '//ul[@id="auto-trail-block"]//a',
                'follow': '//ul[@class="pagination b3"]//li/a'
            },
            {
                'link': 'http://www.topix.com/family',
                'select': r'/family/'
            },
            {
                'link': 'http://www.cbc.ca/news/community',
                'select': r'community'
            }
        ]
    },
    {
        'category': 'Sports & Fitness',
        'data': [
            {
                'link': 'http://www.rotoworld.com/',
                'select': 'all'
            },
            {
                'link': 'http://espn.go.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.fitnessmagazine.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.mensfitness.com/',
                'select': 'all'
            }
        ]
    },
    {
        'category': 'Home & Garden',
        'data': [
            {
                'link': 'http://www.bhg.com/',
                'select': 'all'
            },
            {
                'link': 'http://www.houseandgarden.co.uk/',
                'select': 'all'
            },
            {
                'link': 'http://www.housetohome.co.uk/',
                'select': 'all'
            },
            {
                'link': 'https://au.lifestyle.yahoo.com/better-homes-gardens/',
                'select': r'/better-homes-gardens/'
            }
        ]
    },
    {
        'category': 'Computers & Consumer Electronics',
        'data': [
            {
                'link': 'http://www.computerworld.com/',
                'select': r'/article/'
            },
            {
                'link': 'http://www.pcmag.com/',
                'select': r'article'
            },
            {
                'link': 'http://www.extremetech.com/',
                'select': '/extreme|deal/'
            },
            {
                'link': 'http://www.cnet.com/news/',
                'select': r'news'
            }
        ]
    },
    {
        'category': 'Hobbies & Leisure',
        'data': [
            {
                'link': 'http://www.topix.com/hobbies',
                'select': r'/hobbies/'
            },
            {
                'link': 'http://www.foxnews.com/leisure/index.html',
                'select': r'/leisure/'
            },
            {
                'link': 'http://abc7news.com/topic/hobbies/',
                'select': r'/hobbies/'
            },
            {
                'link': 'http://6abc.com/topic/hobbies/',
                'select': r'/hobbies/'
            }
        ]
    },
    {
        'category': 'Health',
        'data': [
            {
                'link': 'http://www.health.com/health/',
                'select': r'/health/'
            },
            {
                'link': 'http://edition.cnn.com/HEALTH/',
                'select': r'/health/'
            },
            {
                'link': 'http://www.bbc.com/news/health/',
                'select': r'/news/health'
            }
        ]
    },
    {
        'category': 'Business & Industrial',
        'data': [
            {
                'link': 'http://www.bbc.com/news/business/',
                'select': r'/news/business'
            },
            {
                'link': 'http://www.theguardian.com/uk/business',
                'select': r'/business/'
            },
            {
                'link': 'http://www.huffingtonpost.com/business/',
                'select': r'ref=business'
            }
        ]
    }
]
