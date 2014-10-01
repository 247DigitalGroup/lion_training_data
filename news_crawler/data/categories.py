""" selected websites by categories """

CATEGORIES = [
    {
        'category': 'Retailers & General Merchandise',
        'data': [
            {
                'link': 'http://www.cspnet.com/category-news/general-merchandise',
                'xpath': '//div[@class="field__item even"]//a[contains(@href, "general-merchandise")]',
                'follow': '//li[@class="pager__item"]//a'
            },
            {
                'link': 'http://www.retailgazette.co.uk/retail-feature-articles',
                'xpath': '//div[@class="acticle_body"]//a',
                'follow': '//span[@class="page"]//a'
            },
            {
                'link': 'http://retailingtoday.com/section/retail-news',
                'xpath': '//span[@class="field-content"]//a',
                'follow': '//li[@class="pager-item"]//a'
            },
            {
                'link': 'http://www.theretailbulletin.com/section/retail-solutions/',
                'xpath': '//div[@class="newsListing"]//a',
                'follow': '//ul[@class="pagelinks"]//a'
            },
            {
                'link': 'http://www.essentialretail.com/retail-in-depth',
                'xpath': '//ul[@class="items_list"]//a',
                'follow': '//ul[@class="pagination_items"]//a'
            },
            {
                'link': 'http://supermarketnews.com/taxonomy/term/6726/more',
                'xpath': '//h3[@class="title"]//a',
                'follow': '//li[@class="pager-next last"]//a'
            }
        ]
    },
    {
        'category': 'Dining & Nightlife',
        'data': [
            {
                'link': 'http://www.elitetraveler.com/category/finest-dining/dining-news/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="nav-previous"]/a',
            },
            {
                'link': 'http://www.nightclub.com/press-releases',
                'xpath': '//tr[@class="questexcontenttr"]//a',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://nrn.com/taxonomy/term/44074/more',
                'xpath': '//h3[@class="title"]//a',
                'follow': '//ul[@class="pager"]/li/a'
            },
            {
                'link': 'http://ny.eater.com/tags/nightlife',
                'xpath': '//h1[@class="post-title"]//a',
                'follow': '//div[@id="pages"]//a'
            },
            {
                'link': 'http://www.thenynightlife.com/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="nav-previous"]//a'
            },
            {
                'link': 'http://www.northjersey.com/food-and-dining-news/dining-news',
                'xpath': '//div[@class="topicstorytitle"]//a',
                'follow': '//a[@class="morelink1"]'
            },
            {
                'link': 'https://www.finedininglovers.com/blog/news-trends/',
                'xpath': '//a[@class="read-more" and contains(@href, "news-trends")]',
                'follow': '//nav[@class="paginazione"]//a'
            },
            {
                'link': 'http://www.restaurantnews.com/',
                'xpath': '//div[@class="posthead"]//a',
                'follow': '//div[@id="nextprevious"]//a'
            },
        ]
    },
    # {
    #     'category': 'News, Media & Publications',
    #     'data': [
    #         {
    #             'link': 'http://www.buzzfeed.com/news',
    #         },
    #         {
    #             'link': 'http://www.huffingtonpost.com/',
    #             'regex': r'ir=Media'

    #         },
    #         {
    #             'link': 'http://www.opcw.org/news-publications/',
    #             'xpath': '//div[@class="news-text"]//a',
    #             'follow': '//div[@class="browseLinksWrap"]//a'
    #         },
    #         {
    #             'link': 'http://www.mediapost.com/',
    #             'regex': r'/article/'
    #         },
    #         {
    #             'link': 'http://www.wwd.com/media-news/media-features?module=subcat',
    #             'regex': r'media-news',
    #         }
    #     ]
    # },
    {
        'category': 'Real Estate',
        'data':  [
            {
                'link': 'http://profit.ndtv.com/news/real-estate',
                'xpath': '//div[@class="list_intro"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.realtor.com/news/real-estate-news/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="navigation"]//a'
            },
            {
                'link': 'http://www.zillow.com/blog/',
                'xpath': '//h2[@class="title"]//a',
                'follow': '//div[@class="pagination_link more_articles alt_font"]//a'
            },
            # {
            #     'link': 'http://realestate.aol.com/blog/category/news/',
            #     'xpath': '//a[@class="pull-left"]',
            #     'follow': '//a[@rel="next"]'
            # },
            {
                'link': 'http://nypost.com/real-estate/',
                'xpath': '//header[@class="entry-header"]//a',
                'follow': '//div[@class="more-link"]//a'
            },
            {
                'link': 'http://www.propertynews.com/blog/',
                'xpath': '//h2[@class="big no-marg"]//a',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://www.homesandproperty.co.uk/property-news/news/archive',
                'xpath': '//div[@class="field-content field-title"]//a',
                'follow': '//li[@class="pager__item"]//a'
            },
            {
                'link': 'http://uk.reuters.com/news/archive/propertyNews?view=page&page=1',
                'xpath': '//div[@id="blogStyleNews"]//a[contains(@href, "article")]',
                'follow': '//div[@class="pageNavigation"]//a'

            },
            {
                'link': 'http://www.propnews.co.uk/news',
                'xpath': '//div[@class="newsStory"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://therealdeal.com/',
                'xpath': '//h3[@class="entry-title entry-summary"]//a',
                'follow': '//span[@class="next"]//a'
            },
            # {
            #     'link': 'http://www.canadianrealestatemagazine.ca/news',
            #     'xpath': '//h3[@class="catItemTitle"]//a',
            #     'follow': '//div[@class="pagination"]//a'
            # },
            {
                'link': 'http://en.mercopress.com/real-estate',
                'xpath': '//div[@class="item img"]//a',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://rismedia.com/category/real-estate-news/',
                'xpath': '//a[@class="artice-list"]',
                'follow': '//a[@class="page-numbers"]'
            }


        ]
    },
    {
        'category': 'Internet & Telecom',
        'data': [
            {
                'link': 'http://www.budde.com.au/Research/Latest.aspx',
                'xpath': '//ul[@class="ResultList"]//a',
            },
            {
                'link': 'http://www.buddeblog.com.au/',
                'xpath': '//a[@rel="bookmark"]',
                'follow': '//div[@class="navigation"]//a'
            },
            {
                'link': 'http://www.telecomramblings.com/',
                'xpath': '//div[@class="entrybox"]//a',
                'follow': '//div[@class="wp-pagenavi"]//a'
            },
            {
                'link': 'http://www.internetsociety.org/blog/tech-matters',
                'xpath': '//span[@class="field-content"]//a',
                'follow': '//li[@class="pager-next last"]//a'
            },
            {
                'link': 'http://www.telecoms.com/category/format/news/',
                'xpath': '//h2[@class="postTitle"]//a',
                'follow': '//div[@class="pageNavigationLinks"]//a'
            },
            {
                'link': 'http://www.theguardian.com/business/telecoms',
                'xpath': '//div[@class="linktext"]//a',
                'follow': '//ul[@class="pagination b3"]//a'
            },
            {
                'link': 'http://www.websearchguide.ca/internet-news/',
                'xpath': '//h1[@class="entry-title"]//a',
                'follow': '//div[@class="nav-previous"]//a'
            },
            {
                'link': 'http://uk.reuters.com/news/archive/technologyNews?view=page',
                'xpath': '//div[@id="blogStyleNews"]//a[contains(@href, "article")]',
                'follow': '//div[@class="pageNavigation"]//a'
            },
            {
                'link': 'http://www.technewsworld.com/perl/section/internet/?init=22',
                'xpath': '//div[@class="content-block"]//a[contains(@href, "/story/")]',
                'follow': '//a[@class="section-next"]'
            },

        ]
    },
    {
        'category': 'Occasions & Gifts',
        'data': [
            {
                'link': 'http://www.giftsanddec.com/channel/281-gifts',
                'xpath': '//p[@class="title"]//a',
                'follow': '//article[@class="module pagination-next"]//a'
            },
            {
                'link': 'http://www.thinkgeek.com/interests/giftsforhim/?icpg=giftGuide__ForHim',
                'xpath': '//div[@class="product"]//a',
                'follow': '//li[@class="pagenav-item  pagenav-after"]//a'
            },
            {
                'link': 'http://www.thinkgeek.com/interests/giftsforher/?icpg=giftGuide__ForHer',
                'xpath': '//div[@class="product"]//a',
                'follow': '//li[@class="pagenav-item  pagenav-after"]//a'
            },
            {
                'link': 'http://www.thinkgeek.com/interests/giftsforkids/?icpg=giftGuide__ForKids',
                'xpath': '//div[@class="product"]//a',
                'follow': '//li[@class="pagenav-item  pagenav-after"]//a'
            },
            {
                'link': 'http://www.cafepress.com/+fox-news+gifts',
                'xpath': '//div[@class="grid-title"]//a',
                'follow': '//a[@rel="next"]'
            },
            {
                'link': 'http://lifehacker.com/tag/gifts',
                'xpath': '//h1[@class="headline h5 hover-highlight entry-title"]//a',
                'follow': '//div[@class="text-center mbx"]//a'
            },
            {
                'link': 'http://www.buzzfeed.com/tag/gifts',
                'xpath': '//h2[@id="test"]//a',
                'follow': '//ul[@class="paging"]//a'
            },
            {
                'link': 'https://blog.etsy.com/en/?ref=ftr',
                'xpath': '//a[@rel="bookmark"]',
                'follow': '//ul[@class="pages"]//a'
            }
        ]
    },
    {
        'category': 'Jobs & Education',
        'data': [
            {
                'link': 'http://www.indeed.com/jobs?q=&l=Hollywood%2C+FL',
                'xpath': '//h2[@class="jobtitle"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://jobs.bloomberg.com/go/News-Jobs/356821/',
                'xpath': '//a[@class="jobTitle-link"]',
                'follow': '//ul[@class="pagination-links"]//a'
            },
            {
                'link': 'http://jobs.bloomberg.com/go/Experienced-Jobs/515300/',
                'xpath': '//a[@class="jobTitle-link"]',
                'follow': '//ul[@class="pagination-links"]//a'
            },
            {
                'link': 'http://jobs.theguardian.com/searchjobs/',
                'xpath': '//ul[@class="jobsList"]//a',
                'follow': '//a[@class="page"]'
            },
            {
                'link': 'http://www.jobsite.co.uk/jobs/london',
                'xpath': '//div[@class="clearfix"]//a[contains(@href, "/job/")]',
                'follow': '//div[@class="resultsPagination"]//a'
            },
            {
                'link': 'http://www.reed.co.uk/jobs/london',
                'xpath': '//h3[@class="jobTitle"]//a',
                'follow': '//div[@class="pages"]//a'
            }
        ]
    },
    {
        'category': 'Travel & Tourism',
        'data': [
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c7-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c1-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c4-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c0-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c3-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c2-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c5-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c6-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.tripadvisor.com/Inspiration-g1-c8-World.html',
                'xpath': '//dl[@class="inspResults"]//a',
            },
            {
                'link': 'http://www.fodors.com/news/',
                'xpath': '//h2[@class="item-title"]//a',
                'follow': '//div[@class="next"]//a'
            },
            {
                'link': 'http://skift.com/2014/',
                'xpath': '//div[@class="stream-story image"]//a',
                'follow': '//div[@class="stream-jump"]//a'
            },
            {
                'link': 'http://www.businesstravelnews.com/Business-Travel-Stories/',
                'xpath': '//div[@class="item-title"]//a',
                'follow': '//div[@class="pagination right"]//a'
            },
            {
                'link': 'http://www.pattayamail.com/travel',
                'xpath': '//h3[@class="catItemTitle"]//a',
                'follow': '//span[@class="pagination"]//a'

            },
            {
                'link': 'http://www.dailynewsegypt.com/category/touriism/',
                'xpath': '//h2[@class="posttitle"]//a',
                'follow': '//div[@id="nextpage"]//a'
            },
            # {
            #     'link': 'http://www.tourism-review.com/top-weekly-travel-news/1',
            #     'xpath': '//div[@class="block_big_top"]//a',
            #     'follow': '//div[@class="pagination"]//a'
            # }
        ]
    },
    {
        'category': 'Beauty & Personal Care',
        'data': [
            {
                'link': 'http://www.mintel.com/category/press-centre/beauty-and-personal-care',
                'xpath': '//div[@class="post-title-press"]/h2/a',
                'follow': '//div[@class="pagination"]/a'
            },
            {
                'link': 'http://www.dailymail.co.uk/femail/beauty/index.html',
                'regex': 'beauty',
                'follow': '//h2[@class="linkro-darkred"]//a'
            },
            {
                'link': 'http://fashion.telegraph.co.uk/beauty/news-features/',
                'xpath': '//h2[@class="linkro-darkred"]//a',
                'follow': '//a[@id="cphContent_hypMore"]'
            },
            {
                'link': 'http://www.instyle.co.uk/beauty/news',
                'xpath': '//h2[@class="header-link"]/a',
                'follow': '//li[@class="pager-item"]//a'
            },
            {
                'link': 'http://www.allure.com/search?&docType=article',
                'xpath': '//h3[@class="header"]//a',
                'follow': '//span[@class="paginationNext"]//a'
            },
            {
                'link': 'http://www.usmagazine.com/celebrity-beauty/news',
                'xpath': '//div[@class="post-info"]//a',
                'follow': '//div[@class="news-pager"]//a'
            },
            {
                'link': 'http://www.euromonitor.com/beauty-and-personal-care',
                'xpath': '//div[@class="articleListStandard"]//a',
                'follow': '//div[@class="pages"]//a'
            },
            {
                'link': 'http://www.newsforshoppers.com/section/home/personal-care/',
                'xpath': '//div[@class="recent-item"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.beautyworldnews.com/archives/',
                'xpath': '//dd[@class="tit"]//a',
                'follow': '//div[@id="page_num"]//a'
            },
            {
                'link': 'http://www.vogue.com.au/beauty/news/',
                'xpath': '//h3[@class="heading"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.vogue.it/en/beauty/beauty-news',
                'xpath': '//article[@class="spana4"]//a',
                'follow': '//ul[@class="pager inline pull-right"]//a'
            },
            {
                'link': 'http://www.thefashionspot.com/beauty/',
                'xpath': '//a[@class="post-title"]',
                'follow': '//div[@class="wp-pagenavi"]//a'
            },
            {
                'link': 'http://www.elleuk.com/beauty/P0',
                'xpath': '//div[@class="cell-content"]//a[contains(@href, "beauty")]',
                'follow': '//div[@class="pagination module"]//a'
            },
            {
                'link': 'http://hollywoodlife.com/topics/beauty/',
                'xpath': '//a[@class="hl-hp-link"]',
                'follow': '//div[@class="alignright"]//a'
            },
            {
                'link': 'http://www.modernsalon.com/news/',
                'xpath': '//div[@id="dottedbox2"]//a',
                'follow': '//div[@id="tnt_pagination"]//a'
            },
            {
                'link': 'http://www.webmd.com/beauty/news-features',
                'xpath': '//li[@class="type_art"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.latestinbeauty.com/blog/',
                'xpath': '//div[@class="post-heading"]//a',
                'follow': '//div[@class="alignleft"]//a'
            },
            {
                'link': 'http://gulfnews.com/life-style/beauty-fashion',
                'xpath': '//ul[@class="overview noborder"]//a',
                'follow': '//ul[@class="pagination"]//a'
            },
            {
                'link': 'http://www.nowmagazine.co.uk/articles/list/lp/beauty-news',
                'xpath': '//h3[@class="headline"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.mirror.co.uk/3am/style/3am-fashion-celebrity-beauty/',
                'xpath': '//div[@class="teaser-info"]//a[contains(@href, "3am/style")]',
                'follow': '//div[@class="pagination clearfix"]//a'
            },
            {
                'link': 'http://www.marieclaire.co.uk/news/beauty/1.html',
                'xpath': '//div[@class="teaserText"]//a',
                'follow': '//ul[@class="pagination attention"]//a'
            }
        ]

    },
    {
        'category': 'Vehicles',
        'data': [
            {
                'link': 'http://www.autoexpress.co.uk/car-news',
                'xpath': '//div[@class="view-content"]//h2//a',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://www.caranddriver.com/list-news',
                'xpath': '//a[@class="hed"]',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://www.autocar.co.uk/car-news',
                'xpath': '//div[@class="details with-image"]//a',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://www.greencarreports.com/news',
                'xpath': '//div[@class="right-side"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.electric-vehiclenews.com/',
                'xpath': '//h3[@class="post-title entry-title"]//a',
                'follow': '//span[@id="blog-pager-older-link"]//a'
            },
            {
                'link': 'http://www.carwale.com/news/',
                'xpath': '//a[@class="news-title"]',
                'follow': '//div[@id="divStrip"]//a'
            }
        ]
    },
    {
        'category': 'Law & Government',
        'data': [
            {
                'link': 'http://www.hg.org/legal_articles.asp',
                'xpath': '//div[@class="article"]//a'
            },
            {
                'link': 'http://www.law.georgetown.edu/news/',
                'xpath': '//div[@class="article"]//a',
                'follow': '//ul[@class="pagination"]//a'
            },
            {
                'link': 'http://news.msn.com/crime-justice/',
                'xpath': '//li[@class="noimg" or @class="hasimg"]//a'
            },
            {
                'link': 'http://www.abajournal.com/news/',
                'xpath': '//h5[@class="article_list_headline"]//a',
                'follow': '//ul[@class="pagination"]//a'
            },
            {
                'link': 'http://www.lawgazette.co.uk/36.more',
                'xpath': '//div[@class="subSleeve"]//a',
                'follow': '//div[@class="paging_numbers"]//a'
            },
            {
                'link': 'http://www.lawtimesnews.com/headline-news',
                'xpath': '//h2[@class="art-postheader"]//a',
                'follow': '//div[@class="k2Pagination"]//a'
            },
            {
                'link': 'http://abovethelaw.com/government/',
                'xpath': '//h1[@class="postTitle"]//a',
                'follow': '//div[@class="wp-pagenavi clearfix"]//a'
            },
            {
                'link': 'http://www.legalweek.com/category/law-firms',
                'xpath': '//div[@class="common_right_all"]//a',
                'follow': '//a[@class="next_page"]'
            },
        ]
    },
    {
        'category': 'Food & Groceries',
        'data': [
            {
                'link': 'http://www.foodbeast.com/',
                'xpath': '//div[@class="storie_right"]//a',
                'follow': '//ol[@class="wp-paginate"]//li/a'
            },
            {
                'link': 'http://www.independent.co.uk/life-style/food-and-drink/news/',
                'xpath': '//div[@class="text"]//a[contains(@href, "food-and-drink")]',
                'follow': '/div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.foodsafetynews.com/',
                'xpath': '//h2[@class="post-title"]//a',
                'follow': '//li[@class="pagination-old"]//a'
            },
            {
                'link': 'http://www.specialtyfood.com/news-trends/publications/specialty-food-news/',
                'xpath': '//h2[@class="headlines left"]//a',
                'follow': '//span[@class="bold"]//a'
            },
            {
                'link': 'http://www.independent.co.uk/life-style/food-and-drink/news/?pageNumber=1',
                'xpath': '//a[contains(@href, "food-and-drink") and contains(@href, ".html")]',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.supermarketguru.com/food-news-today/',
                'xpath': '//div[@class="artright"]//a',
                'follow': '//div[@class="paging"]//a'
            },
            {
                'link': 'http://www.foodpolitic.com/',
                'xpath': '//div[@class="post-content"]//a',
                'follow': '//div[@class="navigation"]//a'
            },
            {
                'link': 'http://www.chow.com/food-news',
                'xpath': '//h3[@class="blogroll_title"]//a',
                'follow': '//div[@class="wp-pagenavi"]//a'
            },
            {
                'link': 'http://www.foodincanada.com/news/',
                'xpath': '//a[@rel="bookmark"]',
                'follow': '//ul[@class="pagination"]//a'
            }
        ]
    },
    {
        'category': 'Apparel',
        'data': [
            {
                'link': 'http://commonthread.alternativeapparel.com/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//a[@class="page-numbers"]'
            },
            {
                'link': 'http://www.fibre2fashion.com/news/apparel-news/',
                'xpath': '//a[@class="Indexnewstitle"]',
                'follow': '//table[@id="pagingHolder"]//a'
            },
            {
                'link': 'http://apparel.edgl.com/news/all',
                'xpath': '//span[@class="articlenamelinks"]//a',
                'follow': '//div[@class="PagerControl"]//a'
            },
            {
                'link': 'http://jezebel.com/tag/american-apparel',
                'xpath': '//h1[@class="headline h5 hover-highlight entry-title"]//a',
                'follow': '//div[@class="text-center mbx"]//a'
            },
            {
                'link': 'http://www.elle.com/news/fashion-style/',
                'xpath': '//h2[@class="title"]//a',
                'follow': '//a[@rel="archives"]'
            },
            {
                'link': 'http://www.graziadaily.co.uk/fashion/news',
                'xpath': '//div[@class="desc"]//a',
                'follow': '//a[@title="More Stories"]'
            },
            {
                'link': 'http://www.look.co.uk/fashion',
                'xpath': '//div[@class="article_container"]//a[contains(@href, "fashion")]',
                'follow': '//li[@class="pager-item"]//a'
            },
            {
                'link': 'http://www.style.com/trends/fashion',
                'xpath': '//h3[@class="story-item__title"]//a',
                'follow': '//ul[@class="pagination "]//a'
            },
            {
                'link': 'http://www.fashionmagazine.com/tag/fashion-news/',
                'xpath': '//div[@id="featured-cat-sub"]//a',
                'follow': '//nav[@class="pagination"]//a'
            },
            {
                'link': 'http://www.marieclaire.co.uk/news/fashion/1.html',
                'xpath': '//div[@class="teaserText"]//a',
                'follow': '//ul[@class="pagination attention"]//a'
            },
            {
                'link': 'http://www.fashionbeans.com/category/mens-fashion-news/',
                'xpath': '//div[@class="catArticles"]//a',
                'follow': '//a[@class="pageLink"]'
            },
            {
                'link': 'http://blog.freepeople.com/fashion/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://fashionbombdaily.com/category/fashion-news/',
                'xpath': '//div[@class="post_header half"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.gq-magazine.co.uk/style/style-news',
                'xpath': '//a[@class="readLink"]',
                'follow': '//div[@class="page-scroller"]//a'
            },
            {
                'link': 'http://www.ibtimes.co.uk/fashion',
                'xpath': '//div[@class="section-head"]//a',
                'follow': '//div[@class="more-news page-navi"]//a'
            },
            {
                'link': 'http://gizmodo.com/tag/apparel',
                'xpath': '//h1[@class="headline h5 hover-highlight entry-title"]//a',
                'follow': '//div[@class="text-center mbx"]//a'
            },
            {
                'link': 'http://tokyofashion.com/articles/',
                'xpath': '//h3[@class="snippet-title"]//a',
                'follow': '//div[@class="navleft"]//a'
            },
            {
                'link': 'http://www.mixmag.net/fashion/fashion-news',
                'xpath': '//div[@class="node"]//a',
                'follow': '//span[@class="next-atricle-lft"]//a'
            },
            {
                'link': 'http://www.nowmagazine.co.uk/articles/list/lp/fashion-news',
                'xpath': '//h3[@class="headline"]//a',
                'follow': '//div[@class="pagination"]//a'
            }
        ]
    },
    {
        'category': 'Finance',
        'data': [
            {
                'link': 'http://www.financialexpress.com/',
                'xpath': '//div[@class="latestheadlines"]//a',
                'follow': '//div[@class="latestheadlines"]//b/a'
            },
            {
                'link': 'http://www.economist.com/sections/business-finance',
                'xpath': '//div[@class="main-content clearfix section-list"]//a[contains(@href, "finance")]',
                'follow': '//li[@class="pager-item"]//a'
            },
            {
                'link': 'http://www.tradefinancemagazine.com/Channel/23025/Latest-news.html',
                'xpath': '//ul[@class="article_list"]//a',
            },
            {
                'link': 'http://www.structuredfinancenews.com/',
                'xpath': '//div[@id="homeContent"]//a',
                'follow': '//p[@class="more"]//a'
            },
            {
                'link': 'http://www.lse.co.uk/finance-news.asp',
                'xpath': '//a[@class="linkStoryHeadline"]',
                'follow': '//a[@class="linkTabs"]'

            },
            {
                'link': 'http://profit.ndtv.com/news/your-money',
                'xpath': '//div[@class="list_intro"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.sbs.com.au/news/business',
                'xpath': '//div[@class="view-content"]//a',
                'follow': '//ul[@class="pager pager-load-more"]//a'
            },
            {
                'link': 'http://www.investopedia.com/personal-finance/whatsnew/',
                'xpath': '//h3[@class="item-title"]//a[contains(@href, "personal-finance")]',
                'follow': '//li[@class="pager-item"]//a'
            },
            # {
            #     'link': 'http://www.financeasia.com/Category/735,banks.aspx',
            #     'xpath': '//div[@class="article-title"]//a',
            #     'follow': '//div[@class="paging"]//a'
            # },
        ]
    },
    {
        'category': 'Arts & Entertainment',
        'data': [
            {
                'link': 'http://www.eonline.com/news',
                'xpath': '//div[@class="title"]//a',
                'follow': '//div[@class="pageNumbs"]//a'
            },
            {
                'link': 'http://www.digitalspy.co.uk/showbiz/news/',
                'regex': r'/showbiz|movies|music|bollywood|tv|ustv|/.+.html',
                'follow': '//a[@title="Next"]'
            },
            {
                'link': 'http://www.artnews.com/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="nav-previous"]//a'
            },
            {
                'link': 'http://www.artnewsblog.com/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="navigation"]//a'
            },
            {
                'link': 'http://www.theguardian.com/artanddesign/art',
                'xpath': '//ul[@class="list"]//a[contains(@href , "artanddesign")]',
                'follow': '//ul[@class="pagination b3"]//a'
            },
            {
                'link': 'http://www.usmagazine.com/entertainment/news',
                'xpath': '//div[@class="post-info"]//a',
                'follow': '//a[@class="next"]'
            },
            {
                'link': 'http://www.thehollywoodgossip.com/',
                'xpath': '//article//a[@itemprop="url"]',
                'follow': '//nav[@class="pagination pagination-centered"]//a'
            },
            {
                'link': 'http://www.justjared.com/',
                'xpath': '//div[@class="post"]//a[@rel="bookmark"]',
                'follow': '//div[@class="wp-pagenavi"]//a'
            }
        ]
    },
    {
        'category': 'Family & Community',
        'data': [
            {
                'link': 'http://www.netfamilynews.org/',
                'xpath': '//h2[@class="title"]//a',
                'follow': '//div[@class="alignleft"]/a'
            },
            {
                'link': 'http://www.deseretnews.com/family',
                'xpath': '//h2[@class="feature-headline"]//a',
                'follow': '//div[@class="content-pages"]//a'
            },
            {
                'link': 'http://famvin.org/en/',
                'xpath': '//h2[@class="title entry-title"]//a',
                'follow': '//a[@class="page-numbers"]'
            },
            {
                'link': 'http://spousebuzz.com/blog/category/spouse-family-news',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="navigation"]//a'
            },
            {
                'link': 'http://www.tv.com/shows/community/news/',
                'xpath': '//h3[@class="title"]//a',
                'follow': '//span[@class="pages"]//a'
            },
            {
                'link': 'http://www.deseretnews.com/top/family',
                'xpath': '//div[@class="headline-item"]//a',
                'follow': '//div[@class="content-pages"]//a'
            },
            {
                'link': 'http://www.mnn.com/family/family-activities',
                'xpath': '//h2[@class="node-title"]//a',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://www.mnn.com/family/babies-pregnancy',
                'xpath': '//h2[@class="node-title"]//a',
                'follow': '//ul[@class="pager"]//a'
            }

        ]
    },
    {
        'category': 'Sports & Fitness',
        'data': [
            {
                'link': 'http://www.theguardian.com/football/football-league-blog',
                'xpath': '//div[@class="linktext"]//a[contains(@href, "football")]',
                'follow': '//ul[@class="pagination b3"]//a'
            },
            {
                'link': 'http://www.theguardian.com/uk/sport',
                'xpath': '//a[@class="link-text" and contains(@href, "sport")]',
            },
            {
                'link': 'http://www.foxsports.com.au/breaking-news',
                'xpath': '//h3[@class="latest-news-header"]//a',
            },
            {
                'link': 'http://www.theguardian.com/lifeandstyle/fitness',
                'xpath': '//ul[@id="auto-trail-block"]//a[contains(@href, "the-running-blog")]',
                'follow': '//ul[@class="pagination b3"]//a'
            },
            {
                'link': 'http://www.foxsports.com/news',
                'xpath': '//a[@class="buzzer-title-link"]',
                'follow': '//span[@class="pagenumbers"]//a'
            },
            {
                'link': 'http://www.telegraph.co.uk/sport/',
                'regex': '/sport/.+.html'
            },
            {
                'link': 'http://talksport.com/football',
                'xpath': '//div[@class="content"]//h2//a',
                'follow': '//ul[@class="pager"]//a'
            },
            {
                'link': 'http://www.mirror.co.uk/sport/football/news/',
                'xpath': '//div[@class="teaser-info"]//a[contains(@href, "football")]',
                'follow': '//ul[@class="clearfix pagination-controls"]//a'
            },
            {
                'link': 'http://www.bodyandsoul.com.au/fitness/workouts/',
                'xpath': '//div[@class="story-block clearfix"]//a',
                'follow': '//ul[@class="pages clearfix"]//a',
            },
            {
                'link': 'http://www.bodyandsoul.com.au/fitness/training+tips/',
                'xpath': '//div[@class="story-block clearfix"]//a',
                'follow': '//ul[@class="pages clearfix"]//a',
            },
            {
                'link': 'http://www.breakingnews.ie/sport/',
                'xpath': '//ul[@id="content"]//h3/a',
            },
            {
                'link': 'http://www.athensnews.com/ohio/articles.sec--40-1-sports-news.html',
                'xpath': '//h1[@rel="title_traslate"]//a',
                'follow': '//div[@class="Pages"]//a'
            }
        ]
    },
    {
        'category': 'Home & Garden',
        'data': [
            {
                'link': 'http://www.bhg.com/',
                'regex': r'/gardening|decorating|home-improvement/.+'
            },
            {
                'link': 'http://www.houseandgarden.co.uk/',
                'regex': r'/interiors|outdoor-spaces/.+'
            },
            {
                'link': 'http://www.telegraph.co.uk/gardening/',
                'regex': 'gardening/.+.html'
            },
            {
                'link': 'http://www.bbg.org/news',
                'xpath': '//h2[@class="clearboth"]//a',
                'follow': '//p[@class="pagination2"]//a'
            },
            {
                'link': 'http://www.theguardian.com/lifeandstyle/gardens',
                'xpath': '//div[@class="linktext"]//a',
                'follow': '//ul[@class="pagination b3"]//a'
            },
            {
                'link': 'http://gardeningnewstoday.com/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://www.amateurgardening.com/top-tips/',
                'xpath': '//h2[@class="entry-title sub-heading"]//a',
                'follow': '//ul[@class="pagination"]//a'
            },
            {
                'link': 'http://www.amateurgardening.com/how-to/',
                'xpath': '//h2[@class="entry-title sub-heading"]//a',
                'follow': '//ul[@class="pagination"]//a'
            },
            {
                'link': 'http://www.independent.co.uk/property/gardening/',
                'xpath': '//div[@class="article news"]//a',
                'follow': '//div[@class="pagination"]//a'
            },
            {
                'link': 'http://timesofindia.indiatimes.com/life-style/home-garden',
                'xpath': '//div[@class="ct1stry"]//a',
                'follow': '//div[@class="pagenumber1"]//a'
            },
            {
                'link': 'http://www.euromonitor.com/home-and-garden',
                'xpath': '//div[@class="articleListStandard"]//a',
                'follow': '//div[@class="pages"]//a'
            },
            {
                'link': 'http://freshome.com/best-of/',
                'xpath': '//div[@class="entry header_post"]//a',
                'follow': '//ul[@class="pages"]//a'
            },
            {
                'link': 'http://www.gardendesign.com/ideas',
                'xpath': '//div[@class="title"]//a',
                'follow': '//li[@class="pager-item"]//a'
            },
            {
                'link': 'http://www.homeandgardenblog.com/',
                'xpath': '//h3[@class="post-title entry-title"]//a',
                'follow': '//a[@class="blog-pager-older-link"]'
            },
            {
                'link': 'http://www.lifestyle.com.au/garden-ideas/',
                'xpath': '//h2[@class="TitleText"]//a',
                'follow': '//span[@class="Button Number"]//a'
            },
            {
                'link': 'http://www.goodshomedesign.com/category/gardens/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//ol[@class="wp-paginate"]//a'
            },
            {
                'link': 'http://www.goodshomedesign.com/category/ideas/',
                'xpath': '//h2[@class="entry-title"]//a',
                'follow': '//ol[@class="wp-paginate"]//a'
            },
            {
                'link': 'http://www.dailynews.com/home-garden',
                'xpath': '//h3[@class="title"]//a',
                'follow': '//a[contains(@href, "articlelist")]'
            },
            {
                'link': 'http://homegardeningforbeginners.org/',
                'xpath': '//div[@class="box-post-content"]//a',
                'follow': '//div[@class="more_entries"]//a'
            },
            {
                'link': 'http://www.rd.com/home/',
                'xpath': '//a[@class="quick-reads-title"]',
                'follow': '//a[@class="rd-red-buttons"]'
            },
            {
                'link': 'http://realestate.msn.com/HomeAndGarden/index.aspx',
                'xpath': '//ul[@class="linklist3"]//a'
            },
            {
                'link': 'http://www.housetohome.co.uk/articles/greenliving.html',
                'xpath': '//ul[@class="article_container "]//a',
                'follow': '//ul[@class="pagination "]//a'
            },
            {
                'link': 'http://www.utsandiego.com/news/entertainment/lifestyle/home-and-garden/',
                'xpath': '//div[@class="content"]//a[contains(@href, "/news/")]',
                'follow': '//a[@rel="next"]'
            },
            {
                'link': 'http://www.cambridge-news.co.uk/homes-and-gardens',
                'xpath': '//h3[@class="heading heading--l"]//a',
                'follow': '//div[@class="pagination-wrapper"]//a'
            },
            {
                'link': 'http://www.sacbee.com/home_garden/v-all_stories/index.html',
                'xpath': '//div[@class="story clearfix autohighlights"]//div[@class="title"]//a',
                'follow': '//div[@class="spill_navigation pagination"]//a'
            }

        ]
    },
    {
        'category': 'Computers & Consumer Electronics',
        'data': [
            {
                'link': 'http://www.computerworld.com/news',
                'xpath': '//div[@class="post-cont"]//a',
                'follow': '//a[@id="load-more-index"]'
            },
            {
                'link': 'http://www.pcmag.com/reviews',
                'xpath': '//div[@class="title"]//a',
                'follow': '//div[@id="paging"]//a'
            },
            {
                'link': 'http://www.extremetech.com/',
                'xpath': '//div[@class="description"]/a',
                'follow': '//a[@class="btn-prev"]'
            },
            {
                'link': 'http://www.electronicsweekly.com/news/',
                'xpath': '//h2[@class="post-title"]//a',
                'follow': '//div[@class="pagenation clearfix"]//a'
            },
            {
                'link': 'http://www.newelectronics.co.uk/latest-electronics-news/',
                'xpath': '//h2[@itemprop="headline"]//a',
                'follow': '//a[@class="pc_Text"]'
            }
        ]
    },
    # {
    #     'category': 'Hobbies & Leisure',
    #     'data': [
    #         {
    #             'link': 'http://abc7news.com/topic/hobbies/',
    #             'regex': r'/hobbies/'
    #         },
    #         {
    #             'link': 'http://www.leisureopportunities.co.uk/detail.cfm?pagetype=news&subject=NONE',
    #             'regex': '//span[@class="a2"]/a',
    #             'follow': '//span[@class="style125"]/a'
    #         },
    #         {
    #             'link': 'http://www.economist.com/topics/hobbies-and-pastimes',
    #             'regex': '//p[@class="topic-item-title"]//a',
    #             'follow': '//li[@class="pager-item even"]/a'
    #         }
    #     ]
    # },
    {
        'category': 'Health',
        'data': [
            {
                'link': 'http://news.health.com/',
                'xpath': '//h2[@class="blog-post-title"]//a',
                'follow': '//li[@class="btn-next"]//a',
            },
            {
                'link': 'http://www.medicalnewstoday.com/archive/1',
                'regex': r'/articles/.+.php',
                'follow': '//ul[@class="pagination"]//a'
            },
            {
                'link': 'http://www.nlm.nih.gov/medlineplus/newsbydate.html',
                'xpath': '//div[@class="items"]//a'
            }
        ]
    },
    {
        'category': 'Business & Industrial',
        'data': [
            {
                'link': 'http://www.huffingtonpost.com/business/',
                'regex': r'.html?utm_hp_ref=business',
            },
            {
                'link': 'http://www.entrepreneur.com/startingabusiness/businessideas/index.html',
                'xpath': '//div[@class="block"]//a[contains(@href, "article")]',
                'follow': '//div[@class="paging"]//a'
            },
            {
                'link': 'http://news.thomasnet.com/IMT/',
                'xpath': '//a[@rel="bookmark"]',
                'follow': '//div[@style="margin-left: 80px; margin-top:18px;"]//a'
            },
            {
                'link': 'http://www.ien.com/articles/industry-news',
                'xpath': '//div[@class="headline"]//a',
                'follow': '//div[@class="pagin paginBottom"]//a'
            },
            {
                'link': 'http://www.qsrmagazine.com/news',
                'xpath': '//span[@class="field-content"]//a',
                'follow': '//li[@class="pager-next last"]//a'
            },
            {
                'link': 'http://www.techspot.com/category/industry/',
                'xpath': '//div[@class="article-content  "]//a',
                'follow': '//div[@class="footerPagelist comments-pager"]//a'
            },
            {
                'link': 'http://www.eventindustrynews.co.uk/category/brand-marketing/',
                'xpath': '//h2[@class="post-title"]//a',
                'follow': '//a[@class="page-numbers"]'
            },
            {
                'link': 'http://www.euronews.com/business/',
                'xpath': '//ul[@class="subcategoryList clear"]//a',
            },
            {
                'link': 'http://www.ibtimes.co.uk/business',
                'xpath': '//div[@class="section-head"]//a',
                'follow': '//div[@class="more-news"]//a'
            },
            {
                'link': 'http://www.channelnewsasia.com/archives/business',
                'xpath': '//div[@class="txt-box"]//a[contains(@href, "business")]',
                'follow': '//div[@class="archive-pagination"]//a'
            }

        ]
    },
]
