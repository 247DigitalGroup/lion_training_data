""" selected websites by categories """

CATEGORIES = [
    {
        'category': 'Retailers & General Merchandise',
        'data': [
            {
                'link': 'http://www.cspnet.com/category-news/general-merchandise',
                'regex': r'/general-merchandise/'
            },
            {
                'link': 'http://www.retailgazette.co.uk/',
                'regex': r'/articles/'
            },
            {
                'link': 'http://retailingtoday.com/',
                'regex': r'/article/'
            },
            {
                'link': 'http://www.theretailbulletin.com/',
                'regex': r'news'
            }
        ]
    },
    {
        'category': 'Dining & Nightlife',
        'data': [
            {
                'link': 'http://www.elitetraveler.com/category/finest-dining/dining-news/',
                'regex': r'/dining-news/',
                'follow': '//div[@class="nav-previous"]/a',
            },
            {
                'link': 'http://www.nightclub.com/press-releases',
                'regex': r'press-releases',
                'follow': '//ul[@class="pager"]/li/a'
            },
            {
                'link': 'http://nrn.com/taxonomy/term/44074/more',
                'regex': r'/food-trends|casual-dining|franchising|consumer-trends|mergers-acquisitions/',
                'follow': '//ul[@class="pager"]/li/a'
            },
            {
                'link': 'http://go.dallasnews.com/dining/',
                'regex': r'/dining/',
                'follow': '//ul[@class="pagination"]/li/a'
            }
        ]
    },
    {
        'category': 'News, Media & Publications',
        'data': [
            {
                'link': 'http://mashable.com/',
                'regex': r'/\d+/\d+/\d+/.+'
            },
            {
                'link': 'http://www.buzzfeed.com/',
            },
            {
                'link': 'http://www.nytimes.com/',
            },
            {
                'link': 'http://www.huffingtonpost.com/',
            },
            {
                'link': 'http://techcrunch.com/',
            }
        ]
    },
    {
        'category': 'Real Estate',
        'data':  [
            {
                'link': 'http://www.zillow.com/san-francisco-ca/rentals/',
                'regex': r'/b/.+_ll/|/homedetails.+_zpid/',
                'follow': '//ul[@class="pagination-2012 zbti"]/li/a'
            },
            {
                'link': 'http://www.realestate.com.au/blog/news/',
                'regex': r'/blog/',
                'follow': '//div[@class="wp-pagenavi"]/a'
            },
            {
                'link': 'http://www.realtor.com/apartments/Los-Angeles_CA',
                'regex': r'/realestateandhomes-detail/',
                'follow': '//ol[@class="pagination pagination-pos-b"]/li/a'
            },
            {
                'link': 'http://www.worldpropertychannel.com/',
                'regex': r'/north-america-residential-news/'
            }
        ]
    },
    {
        'category': 'Internet & Telecom',
        'data': [
            {
                'link': 'http://www.telecompaper.com/international/news/internet',
                'regex': r'/news/',
            },
            {
                'link': 'http://www.budde.com.au/',
                'regex': 'all'
            },
            {
                'link': 'http://www.telecomramblings.com/',
            },
            {
                'link': 'http://www.internetnews.com/',
            },
            {
                'link': 'http://www.internet.com/',
            }
        ]
    },
    {
        'category': 'Occasions & Gifts',
        'data': [
            {
                'link': 'http://www.buyagift.co.uk/',
            },
            {
                'link': 'http://www.lovelygifts.com/',
            },
            {
                'link': 'http://www.harryanddavid.com/',
            }
        ]
    },
    {
        'category': 'Jobs & Education',
        'data': [
            {
                'link': 'http://www.indeed.com/l-Seattle,-WA-jobs.html',
            },
            {
                'link': 'http://www.glassdoor.com/Job/jobs.htm',
            },
            {
                'link': 'http://jobsearch.monster.com/browse/?sf=14',
                'regex': r'/jobview.monster.com/',
                'follow': '//span[@class="navLinks"]//a'
            },
            {
                'link': 'http://www.huffingtonpost.com/education/',
                'regex': r'utm_hp_ref=education'
            },
            {
                'link': 'http://www.theguardian.com/education',
                'regex': r'/education/'
            },
        ]
    },
    {
        'category': 'Travel & Tourism',
        'data': [
            {
                'link': 'http://www.tripadvisor.com/',
            },
            {
                'link': 'http://www.expedia.com/?rfrr=Header.POSRedirect.www.expedia.com.vn%252FHome.htm',
            },
            {
                'link': 'http://www.kayak.com/',
            },
            {
                'link': 'http://www.travelpulse.com/news/',
                'regex': r'news'
            },
            {
                'link': 'http://www.telegraph.co.uk/travel/travelnews/',
                'regex': r'travel'
            },
        ]
    },
    {
        'category': 'Beauty & Personal Care',
        'data': [
            {
                'link': 'http://www.euromonitor.com/beauty-and-personal-care',
            },
            {
                'link': 'http://www.mintel.com/category/press-centre/beauty-and-personal-care',
                'xpath': '//div[@class="post-title-press"]/h2/a',
                'follow': '//div[@class="pagination"]/a'
            },
            {
                'link': 'http://www.dowcorning.com/',
            }
        ]

    },
    {
        'category': 'Vehicles',
        'data': [
            {
                'link': 'http://www.gm.com/vehicles/browseByType.html',
            },
            {
                'link': 'http://www.usedcars.com/',
            },
            {
                'link': 'http://www.autotrader.com/',
            }
        ]
    },
    {
        'category': 'Law & Government',
        'data': [
            {
                'link': 'http://www.hg.org/',
            },
            {
                'link': 'http://www.theguardian.com/law',
                'regex': r'/law/'
            },
            {
                'link': 'http://www.bloomberg.com/news/law/',
                'regex': r'/news/',
                'follow': '//ul[@section_name="more_LAW"]//li//a'
            },
            {
                'link': 'http://www.law.com/',
                'regex': r'/sites/articles/',
            }
        ]
    },
    {
        'category': 'Food & Groceries',
        'data': [
            {
                'link': 'http://www.foodbeast.com/',
            },
            {
                'link': 'http://www.independent.co.uk/life-style/food-and-drink/news/',
                'regex': r'/food-and-drink/',
                'follow': '/div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.foodsafetynews.com/',
            },
            {
                'link': 'http://www.sciencedaily.com/news/plants_animals/food/',
                'xpath': '//div[@class="section_headlines"]//a',
                'follow': '//div[@id="summaries_button"]/a'
            },
            {
                'link': 'http://www.specialtyfood.com/news-trends/publications/specialty-food-news/',
                'regex': r'article',
                'follow': '//span[@class="bold"]//a'
            },
        ]
    },
    {
        'category': 'Apparel',
        'data': [
            {
                'link': 'http://www.americanapparel.net/',
            },
            {
                'link': 'http://www.alternativeapparel.com/',
            },
            {
                'link': 'http://www.zappos.com/',
            }
        ]
    },
    {
        'category': 'Finance',
        'data': [
            {
                'link': 'http://www.efinancialnews.com/',
            },
            {
                'link': 'http://www.reuters.com/finance',
                'regex': r'/article/'
            },
            {
                'link': 'http://www.bloomberg.com/news/finance/',
            }
        ]
    },
    {
        'category': 'Arts & Entertainment',
        'data': [
            {
                'link': 'http://www.bbc.com/news/entertainment_and_arts/',
                'regex': r'/news/entertainment-arts'
            },
            {
                'link': 'http://www.telegraph.co.uk/culture/',
                'regex': r'/culture/'
            },
            {
                'link': 'http://www.independent.co.uk/arts-entertainment/',
                'regex': r'arts-entertainment'
            },
            {
                'link': 'http://www.eonline.com/',
                'regex': r'news'
            }
        ]
    },
    {
        'category': 'Family & Community',
        'data': [
            {
                'link': 'http://www.theguardian.com/lifeandstyle/family',
                'xpath': '//ul[@id="auto-trail-block"]//a',
                'follow': '//ul[@class="pagination b3"]//li/a'
            },
            {
                'link': 'http://www.topix.com/family',
                'regex': r'/family/'
            },
            {
                'link': 'http://www.cbc.ca/news/community',
                'regex': r'community'
            }
        ]
    },
    {
        'category': 'Sports & Fitness',
        'data': [
            {
                'link': 'http://www.rotoworld.com/',
            },
            {
                'link': 'http://espn.go.com/',
            },
            {
                'link': 'http://www.fitnessmagazine.com/',
            },
            {
                'link': 'http://www.mensfitness.com/',
            }
        ]
    },
    {
        'category': 'Home & Garden',
        'data': [
            {
                'link': 'http://www.bhg.com/',
            },
            {
                'link': 'http://www.houseandgarden.co.uk/',
            },
            {
                'link': 'http://www.housetohome.co.uk/',
            },
            {
                'link': 'https://au.lifestyle.yahoo.com/better-homes-gardens/',
                'regex': r'/better-homes-gardens/'
            }
        ]
    },
    {
        'category': 'Computers & Consumer Electronics',
        'data': [
            {
                'link': 'http://www.computerworld.com/',
                'regex': r'/article/'
            },
            {
                'link': 'http://www.pcmag.com/',
                'regex': r'article'
            },
            {
                'link': 'http://www.extremetech.com/',
                'regex': '/extreme|deal/'
            },
            {
                'link': 'http://www.cnet.com/news/',
                'regex': r'news'
            }
        ]
    },
    {
        'category': 'Hobbies & Leisure',
        'data': [
            {
                'link': 'http://www.topix.com/hobbies',
                'regex': r'/hobbies/'
            },
            {
                'link': 'http://www.foxnews.com/leisure/index.html',
                'regex': r'/leisure/'
            },
            {
                'link': 'http://abc7news.com/topic/hobbies/',
                'regex': r'/hobbies/'
            },
            {
                'link': 'http://6abc.com/topic/hobbies/',
                'regex': r'/hobbies/'
            }
        ]
    },
    {
        'category': 'Health',
        'data': [
            {
                'link': 'http://www.health.com/health/',
                'regex': r'/health/'
            },
            {
                'link': 'http://edition.cnn.com/HEALTH/',
                'regex': r'/health/'
            },
            {
                'link': 'http://www.bbc.com/news/health/',
                'regex': r'/news/health'
            }
        ]
    },
    {
        'category': 'Business & Industrial',
        'data': [
            {
                'link': 'http://www.bbc.com/news/business/',
                'regex': r'/news/business'
            },
            {
                'link': 'http://www.theguardian.com/uk/business',
                'regex': r'/business/'
            },
            {
                'link': 'http://www.huffingtonpost.com/business/',
                'regex': r'ref=business'
            }
        ]
    }
]
