
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>大数据分析@唐松</title>
<meta name="description" content="唐松的个人博客，分享大数据分析和 Python 网络爬虫的思考。" />
<meta name="keywords" content="唐松, Santos, 博客" />
<link rel="shortcut icon" href="http://www.santostang.com/wp-content/themes/SongStyle-Two/images/favicon.ico" type="image/x-icon" />
<link rel="stylesheet" href="http://www.santostang.com/wp-content/themes/SongStyle-Two/css/bootstrap.min.css">
<link rel="stylesheet" href="http://www.santostang.com/wp-content/themes/SongStyle-Two/css/font-awesome.min.css">
<script type="text/javascript" src="http://www.santostang.com/wp-content/themes/SongStyle-Two/js/jquery.min.js"></script>
<script type="text/javascript" src="http://www.santostang.com/wp-content/themes/SongStyle-Two/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="http://www.santostang.com/wp-content/themes/SongStyle-Two/style.css">
<link rel="pingback" href="http://www.santostang.com/xmlrpc.php" />
<link rel='dns-prefetch' href='//s.w.org' />
<link rel='stylesheet' id='crayon-css'  href='http://www.santostang.com/wp-content/plugins/crayon-syntax-highlighter/css/min/crayon.min.css?ver=_2.7.2_beta' type='text/css' media='all' />
<link rel='stylesheet' id='crayon-theme-classic-css'  href='http://www.santostang.com/wp-content/plugins/crayon-syntax-highlighter/themes/classic/classic.css?ver=_2.7.2_beta' type='text/css' media='all' />
<link rel='stylesheet' id='crayon-font-monaco-css'  href='http://www.santostang.com/wp-content/plugins/crayon-syntax-highlighter/fonts/monaco.css?ver=_2.7.2_beta' type='text/css' media='all' />
<link rel='https://api.w.org/' href='http://www.santostang.com/wp-json/' />
<script type="text/javascript" src="http://www.santostang.com/wp-content/plugins/si-captcha-for-wordpress/captcha/si_captcha.js?ver=1522761665"></script>
<!-- begin SI CAPTCHA Anti-Spam - login/register form style -->
<style type="text/css">
.si_captcha_small { width:175px; height:45px; padding-top:10px; padding-bottom:10px; }
.si_captcha_large { width:250px; height:60px; padding-top:10px; padding-bottom:10px; }
img#si_image_com { border-style:none; margin:0; padding-right:5px; float:left; }
img#si_image_reg { border-style:none; margin:0; padding-right:5px; float:left; }
img#si_image_log { border-style:none; margin:0; padding-right:5px; float:left; }
img#si_image_side_login { border-style:none; margin:0; padding-right:5px; float:left; }
img#si_image_checkout { border-style:none; margin:0; padding-right:5px; float:left; }
img#si_image_jetpack { border-style:none; margin:0; padding-right:5px; float:left; }
img#si_image_bbpress_topic { border-style:none; margin:0; padding-right:5px; float:left; }
.si_captcha_refresh { border-style:none; margin:0; vertical-align:bottom; }
div#si_captcha_input { display:block; padding-top:15px; padding-bottom:5px; }
label#si_captcha_code_label { margin:0; }
input#si_captcha_code_input { width:65px; }
p#si_captcha_code { clear: left; padding-top:10px; }
.si-captcha-jetpack-error { color:#DC3232; }
</style>
<!-- end SI CAPTCHA Anti-Spam - login/register form style -->
</head>

<body>
<header id="header">
  <div class="avatar"><img src="http://www.santostang.com/wp-content/themes/SongStyle-Two/images/avatar.jpg" alt="数据科学@唐松Santos" class="img-circle" width="50%"></div>
  <h3 id="name">数据科学@唐松Santos</h3>
  <div class="sns">
    <a href="http://www.santostang.com/feed/" target="_blank" rel="nofollow" title="RSS"><i class="fa fa-rss" aria-hidden="true"></i></a>
        <a href="http://weibo.com/santostang" target="_blank" rel="nofollow" title="Weibo"><i class="fa fa-weibo" aria-hidden="true"></i></a>
                <a href="https://www.linkedin.com/in/santostang" target="_blank" rel="nofollow" title="Linkedin"><i class="fa fa-linkedin" aria-hidden="true"></i></a>
                <a href="mailto:tangsongsky@gmail.com" target="_blank" rel="nofollow" title="envelope"><i class="fa fa-envelope" aria-hidden="true"></i></i></a>
          </div>
  <div class="nav">
   <ul><li class="current-menu-item"><a href="http://www.santostang.com/">首页</a></li>
<li><a href="http://www.santostang.com/about-me/">关于我</a></li>
<li><a href="http://www.santostang.com/scrapy_code/">爬虫代码</a></li>
<li><a href="http://www.santostang.com/wp-login.php">登录</a></li>
</ul>  </div>
</header>
<div id="main">
  <div class="row box">
    <div class="col-md-8">
                  <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/10/23/%e3%80%8a%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab%ef%bc%9a%e4%bb%8e%e5%85%a5%e9%97%a8%e5%88%b0%e5%ae%9e%e8%b7%b5%e3%80%8b%e4%b8%80%e4%b9%a6%e5%8b%98%e8%af%af/">《网络爬虫：从入门到实践》一书勘误</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 10月23日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/big-data-marketing/" rel="category tag">大数据营销</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/10/23/%e3%80%8a%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab%ef%bc%9a%e4%bb%8e%e5%85%a5%e9%97%a8%e5%88%b0%e5%ae%9e%e8%b7%b5%e3%80%8b%e4%b8%80%e4%b9%a6%e5%8b%98%e8%af%af/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> </span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>本书由于是第一版，因此还存在一些差错，希望各位读者谅解。

另外，感谢各位读者的指正，现将本书的错误之处一并放在此处，方便其他读者更好阅读和使用此书。也欢迎大家在知乎私信或者留言给我，我会持续更新此...</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/10/22/%e5%9b%bd%e5%86%85%e4%b8%8b%e8%bd%bdanaconda%e9%80%9f%e5%ba%a6%e6%85%a2%ef%bc%8c%e8%af%b7%e4%bd%bf%e7%94%a8%e6%b8%85%e5%8d%8e%e9%95%9c%e5%83%8f/">国内下载Anaconda速度慢，请使用清华镜像</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 10月22日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/python_web_scrappy/" rel="category tag">python 网络爬虫</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/10/22/%e5%9b%bd%e5%86%85%e4%b8%8b%e8%bd%bdanaconda%e9%80%9f%e5%ba%a6%e6%85%a2%ef%bc%8c%e8%af%b7%e4%bd%bf%e7%94%a8%e6%b8%85%e5%8d%8e%e9%95%9c%e5%83%8f/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> </span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>近日，有不少读者反映，我在书中给出的 Anaconda 链接无法访问，或者下载超过了几个小时。

这是因为祖国的 GFW 啊，访问国外网站始终很慢。有这个问题请大家使用清华大学的镜像吧，链接：
https://mirrors.tuna....</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/09/25/4-3-%e9%80%9a%e8%bf%87-selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/">4.3 通过 selenium 模拟浏览器抓取</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 09月25日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/big-data-marketing/" rel="category tag">大数据营销</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/09/25/4-3-%e9%80%9a%e8%bf%87-selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> </span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>4&#46;3 通过 selenium 模拟浏览器抓取

在之前的例子中，使用 Chrome 的“检查”功能找到源地址十分容易，但是有一些网站非常复杂，如天猫产品评论，使用“检查”功能很难找到调用的网页地址。除此之外，有一些数据...</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/09/25/4-2-%e8%a7%a3%e6%9e%90%e7%9c%9f%e5%ae%9e%e5%9c%b0%e5%9d%80%e6%8a%93%e5%8f%96/">4.2 解析真实地址抓取</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 09月25日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/big-data-marketing/" rel="category tag">大数据营销</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/09/25/4-2-%e8%a7%a3%e6%9e%90%e7%9c%9f%e5%ae%9e%e5%9c%b0%e5%9d%80%e6%8a%93%e5%8f%96/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> </span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>4&#46;2 解析真实地址抓取

虽然数据并没有出现在网页源代码中，我们也可以找到数据的真实地址，请求这个真实地址也可以获得想要的数据。这里用到浏览器的“检查”功能。 下面以笔者博客的“Hello World”文章为例，...</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/09/25/4-1-%e5%8a%a8%e6%80%81%e6%8a%93%e5%8f%96%e7%9a%84%e5%ae%9e%e4%be%8b/">4.1 动态抓取的实例</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 09月25日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/big-data-marketing/" rel="category tag">大数据营销</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/09/25/4-1-%e5%8a%a8%e6%80%81%e6%8a%93%e5%8f%96%e7%9a%84%e5%ae%9e%e4%be%8b/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> </span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>4.1 动态抓取的实例

在开始爬取动态网页前，我们还需要了解一种异步更新技术— AJAX(Asynchronous Javascript And XML，异步 JavaScript 和 XML)。它的价值在于通过在后台与服务器进行少量数据交换就可以使网页实...</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/03/08/hello-python/">Hello Python!</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 03月08日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/big-data-marketing/" rel="category tag">大数据营销</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/03/08/hello-python/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> </span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>This is an article for testing. I use it to show the example in my book Web Scrappy by Python.
Test
</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/03/07/echarts%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b02-%e5%8d%95%e9%a1%b5%e9%9d%a2%e5%a4%9a%e5%bc%a0%e5%9b%be%e8%a1%a8/">echarts学习笔记(2) &#8212; 同一页面多图表</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 03月07日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/big-data-marketing/" rel="category tag">大数据营销</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/03/07/echarts%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b02-%e5%8d%95%e9%a1%b5%e9%9d%a2%e5%a4%9a%e5%bc%a0%e5%9b%be%e8%a1%a8/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> </span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>本文首发于 CSDN，当年，也就是2014年，我还是在大四的最后一个暑假，在 EMC 做实习，用 echarts做一个可视化的工具。

在一个页面只是一个图表很简单，如果要在一个页面中添加多张图的话，怎么办呢？

      

...</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/03/07/echarts%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b01-%e4%bd%bf%e7%94%a8%e6%a8%a1%e5%9d%97%e5%8c%96%e5%8d%95%e6%96%87%e4%bb%b6%e5%bc%95%e5%85%a5/">echarts学习笔记(1) &#8212; 模块化单文件引入</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 03月07日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/%e6%95%b0%e6%8d%ae%e5%8f%af%e8%a7%86%e5%8c%96/" rel="category tag">数据可视化</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/03/07/echarts%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b01-%e4%bd%bf%e7%94%a8%e6%a8%a1%e5%9d%97%e5%8c%96%e5%8d%95%e6%96%87%e4%bb%b6%e5%bc%95%e5%85%a5/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> <a href="http://www.santostang.com/tag/echarts/" rel="tag">Echarts</a>,<a href="http://www.santostang.com/tag/%e5%a4%a7%e6%95%b0%e6%8d%ae/" rel="tag">大数据</a>,<a href="http://www.santostang.com/tag/%e6%95%b0%e6%8d%ae%e5%8f%af%e8%a7%86%e5%8c%96/" rel="tag">数据可视化</a></span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>本文首发于 CSDN，地址为：echarts学习笔记(1)。当年，也就是2014年，我还是在大四的最后一个暑假，在 EMC 做实习，用 echarts做一个可视化的工具。

因为最近需要用到echarts来做 BI 商业智能工具, 而echarts相...</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/03/06/%e3%80%90%e7%88%ac%e8%99%ab%e4%ba%8c%e3%80%91%e7%88%ac%e8%99%ab%e7%9a%84%e6%a1%86%e6%9e%b6%e5%92%8c%e5%9f%ba%e6%9c%ac%e8%ae%ae%e9%a2%98/">【爬虫二】爬虫的框架和基本议题</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 03月06日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/python_web_scrappy/" rel="category tag">python 网络爬虫</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/03/06/%e3%80%90%e7%88%ac%e8%99%ab%e4%ba%8c%e3%80%91%e7%88%ac%e8%99%ab%e7%9a%84%e6%a1%86%e6%9e%b6%e5%92%8c%e5%9f%ba%e6%9c%ac%e8%ae%ae%e9%a2%98/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> <a href="http://www.santostang.com/tag/python/" rel="tag">python</a>,<a href="http://www.santostang.com/tag/%e5%a4%a7%e6%95%b0%e6%8d%ae/" rel="tag">大数据</a>,<a href="http://www.santostang.com/tag/%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab/" rel="tag">网络爬虫</a></span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>本文首发于知乎专栏，@唐松。链接：知乎专栏：【爬虫二】爬虫的框架和基本议题

爬虫的技术文章很少有从整体角度来说的，这次就从一个宏观的角度出发，希望通过这篇文章说清楚三个问题：


爬虫的流程是怎样的？
...</p>
        </div>
      </article>
                        <article class="article-list-1 clearfix">
        <header class="clearfix">
          <h1 class="post-title"><a href="http://www.santostang.com/2017/03/06/%e3%80%90%e7%88%ac%e8%99%ab%e4%b8%80%e3%80%91%e6%9c%80%e7%ae%80%e5%8d%95%e7%9a%84%e7%88%ac%e8%99%ab%ef%bc%8c%e9%9b%b6%e5%9f%ba%e7%a1%80%e6%95%99%e5%ad%a6/">【爬虫一】最简单的爬虫，零基础教学</a></h1>
          <div class="post-meta">
            <span class="meta-span"><i class="fa fa-calendar"></i> 03月06日</span>
            <span class="meta-span"><i class="fa fa-folder-open-o"></i> <a href="http://www.santostang.com/category/python_web_scrappy/" rel="category tag">python 网络爬虫</a></span>
            <span class="meta-span"><i class="fa fa-commenting-o"></i> <a href="http://www.santostang.com/2017/03/06/%e3%80%90%e7%88%ac%e8%99%ab%e4%b8%80%e3%80%91%e6%9c%80%e7%ae%80%e5%8d%95%e7%9a%84%e7%88%ac%e8%99%ab%ef%bc%8c%e9%9b%b6%e5%9f%ba%e7%a1%80%e6%95%99%e5%ad%a6/#respond">没有评论</a></span>
            <span class="meta-span hidden-xs"><i class="fa fa-tags" aria-hidden="true"></i> <a href="http://www.santostang.com/tag/python/" rel="tag">python</a>,<a href="http://www.santostang.com/tag/%e5%a4%a7%e6%95%b0%e6%8d%ae/" rel="tag">大数据</a>,<a href="http://www.santostang.com/tag/%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab/" rel="tag">网络爬虫</a></span>
          </div>
        </header>
        <div class="post-content clearfix">
          <p>爬虫在大数据时代占据了重要的位置，在网上有大量的公开数据可以轻松获取。

爬虫入门其实非常简单，就算你是编程小白，也可以轻松爬下一些网站。下面就以爬大众点评 在深圳市搜索潮汕牛肉的结果为例，教大家学会...</p>
        </div>
      </article>
                  <nav style="float:right">
        <ul class='pagination'><li class='active'><a href='http://www.santostang.com/'>1<span class='sr-only'>(current)</span></a></li><li><a href='http://www.santostang.com/page/2/'>2</a></li></ul>
      </nav>
    </div>
    <div class="col-md-4 hidden-xs hidden-sm">
      
<aside class="widget clearfix">
  <form id="searchform" action="http://www.santostang.com">
    <div class="input-group">
      <input type="search" class="form-control" placeholder="搜索…" value="" name="s">
      <span class="input-group-btn">
      <button class="btn btn-default" type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
      </span> </div>
  </form>
</aside>
<aside class="widget clearfix">
  <h4 class="widget-title">文章分类</h4>
  <div class="widget-cat">
    <ul>
      	<li class="cat-item cat-item-3"><a href="http://www.santostang.com/category/python_web_scrappy/" >python 网络爬虫</a> (4)
</li>
	<li class="cat-item cat-item-1"><a href="http://www.santostang.com/category/big-data-marketing/" >大数据营销</a> (6)
</li>
	<li class="cat-item cat-item-9"><a href="http://www.santostang.com/category/%e6%95%b0%e6%8d%ae%e5%8f%af%e8%a7%86%e5%8c%96/" >数据可视化</a> (1)
</li>
    </ul>
  </div>
</aside>
<aside class="widget clearfix">
  <h4 class="widget-title">热门文章</h4>
  <ul class="widget-hot">
    
<li><a href="http://www.santostang.com/2017/10/22/%e5%9b%bd%e5%86%85%e4%b8%8b%e8%bd%bdanaconda%e9%80%9f%e5%ba%a6%e6%85%a2%ef%bc%8c%e8%af%b7%e4%bd%bf%e7%94%a8%e6%b8%85%e5%8d%8e%e9%95%9c%e5%83%8f/" target="_blank" >国内下载Anaconda速度慢，请使用清华镜像</a></li>
<li><a href="http://www.santostang.com/2017/10/23/%e3%80%8a%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab%ef%bc%9a%e4%bb%8e%e5%85%a5%e9%97%a8%e5%88%b0%e5%ae%9e%e8%b7%b5%e3%80%8b%e4%b8%80%e4%b9%a6%e5%8b%98%e8%af%af/" target="_blank" >《网络爬虫：从入门到实践》一书勘误</a></li>  </ul>
</aside>
<aside class="widget clearfix">
  <h4 class="widget-title">随机推荐</h4>
  <ul class="widget-hot">
        <li><a href="http://www.santostang.com/2017/09/25/4-1-%e5%8a%a8%e6%80%81%e6%8a%93%e5%8f%96%e7%9a%84%e5%ae%9e%e4%be%8b/" title="4.1 动态抓取的实例">4.1 动态抓取的实例</a></li>
	    <li><a href="http://www.santostang.com/2017/03/06/%e3%80%90%e7%88%ac%e8%99%ab%e4%b8%80%e3%80%91%e6%9c%80%e7%ae%80%e5%8d%95%e7%9a%84%e7%88%ac%e8%99%ab%ef%bc%8c%e9%9b%b6%e5%9f%ba%e7%a1%80%e6%95%99%e5%ad%a6/" title="【爬虫一】最简单的爬虫，零基础教学">【爬虫一】最简单的爬虫，零基础教学</a></li>
	    <li><a href="http://www.santostang.com/2017/03/07/echarts%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b01-%e4%bd%bf%e7%94%a8%e6%a8%a1%e5%9d%97%e5%8c%96%e5%8d%95%e6%96%87%e4%bb%b6%e5%bc%95%e5%85%a5/" title="echarts学习笔记(1) &#8212; 模块化单文件引入">echarts学习笔记(1) &#8212; 模块化单文件引入</a></li>
	    <li><a href="http://www.santostang.com/2017/09/25/4-3-%e9%80%9a%e8%bf%87-selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/" title="4.3 通过 selenium 模拟浏览器抓取">4.3 通过 selenium 模拟浏览器抓取</a></li>
	    <li><a href="http://www.santostang.com/2017/03/06/%e3%80%90%e7%88%ac%e8%99%ab%e4%ba%8c%e3%80%91%e7%88%ac%e8%99%ab%e7%9a%84%e6%a1%86%e6%9e%b6%e5%92%8c%e5%9f%ba%e6%9c%ac%e8%ae%ae%e9%a2%98/" title="【爬虫二】爬虫的框架和基本议题">【爬虫二】爬虫的框架和基本议题</a></li>
	    <li><a href="http://www.santostang.com/2017/03/07/echarts%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b02-%e5%8d%95%e9%a1%b5%e9%9d%a2%e5%a4%9a%e5%bc%a0%e5%9b%be%e8%a1%a8/" title="echarts学习笔记(2) &#8212; 同一页面多图表">echarts学习笔记(2) &#8212; 同一页面多图表</a></li>
	    <li><a href="http://www.santostang.com/2017/03/02/hello-world/" title="Hello world!">Hello world!</a></li>
	    <li><a href="http://www.santostang.com/2017/10/23/%e3%80%8a%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab%ef%bc%9a%e4%bb%8e%e5%85%a5%e9%97%a8%e5%88%b0%e5%ae%9e%e8%b7%b5%e3%80%8b%e4%b8%80%e4%b9%a6%e5%8b%98%e8%af%af/" title="《网络爬虫：从入门到实践》一书勘误">《网络爬虫：从入门到实践》一书勘误</a></li>
	    <li><a href="http://www.santostang.com/2017/10/22/%e5%9b%bd%e5%86%85%e4%b8%8b%e8%bd%bdanaconda%e9%80%9f%e5%ba%a6%e6%85%a2%ef%bc%8c%e8%af%b7%e4%bd%bf%e7%94%a8%e6%b8%85%e5%8d%8e%e9%95%9c%e5%83%8f/" title="国内下载Anaconda速度慢，请使用清华镜像">国内下载Anaconda速度慢，请使用清华镜像</a></li>
	    <li><a href="http://www.santostang.com/2017/03/08/hello-python/" title="Hello Python!">Hello Python!</a></li>
	  </ul>
</aside>
<aside class="widget clearfix">
  <h4 class="widget-title">标签云</h4>
  <div class="widget-tags">
    <a href='http://www.santostang.com/tag/echarts/' class='tag-link-11 tag-link-position-1' title='1个话题' style="color:#b891c9;font-size: 8pt;;">Echarts</a>
<a href='http://www.santostang.com/tag/python/' class='tag-link-6 tag-link-position-2' title='2个话题' style="color:#53a260;font-size: 16.4pt;;">python</a>
<a href='http://www.santostang.com/tag/%e5%a4%a7%e6%95%b0%e6%8d%ae/' class='tag-link-8 tag-link-position-3' title='3个话题' style="color:#72acac;font-size: 22pt;;">大数据</a>
<a href='http://www.santostang.com/tag/%e6%95%b0%e6%8d%ae%e5%8f%af%e8%a7%86%e5%8c%96/' class='tag-link-10 tag-link-position-4' title='1个话题' style="color:#6bcfd3;font-size: 8pt;;">数据可视化</a>
<a href='http://www.santostang.com/tag/%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab/' class='tag-link-7 tag-link-position-5' title='2个话题' style="color:#52fb76;font-size: 16.4pt;;">网络爬虫</a>  </div>
</aside>
<aside class="widget clearfix">
  <h4 class="widget-title">友情链接</h4>
  <ul class="widget-links">
    <li><a href="http://www.santostang.com/wp-login.php">登录</a></li>
  </ul>
</aside>
    </div>
  </div>
</div>

<footer id="footer">
  <div class="copyright">
    <p><i class="fa fa-copyright" aria-hidden="true"></i> 2017 <b>数据科学@唐松Santos</b></p>
    <p>Powered by <b>WordPress</b>. Theme by <a href="http://tangjie.me/jiestyle" title="JieStyle" target="_blank"><b>JieStyle Two</b></a> | </p>
  </div>
  <div style="display:none;">  </div>
</footer>
<script type="text/javascript" src="http://www.santostang.com/wp-content/themes/SongStyle-Two/js/skel.min.js"></script> 
<script type="text/javascript" src="http://www.santostang.com/wp-content/themes/SongStyle-Two/js/util.min.js"></script> 
<script type="text/javascript" src="http://www.santostang.com/wp-content/themes/SongStyle-Two/js/nav.js"></script>
<script type='text/javascript' src='http://www.santostang.com/wp-includes/js/jquery/jquery.js?ver=1.12.4'></script>
<script type='text/javascript' src='http://www.santostang.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var CrayonSyntaxSettings = {"version":"_2.7.2_beta","is_admin":"0","ajaxurl":"http:\/\/www.santostang.com\/wp-admin\/admin-ajax.php","prefix":"crayon-","setting":"crayon-setting","selected":"crayon-setting-selected","changed":"crayon-setting-changed","special":"crayon-setting-special","orig_value":"data-orig-value","debug":""};
var CrayonSyntaxStrings = {"copy":"Press %s to Copy, %s to Paste","minimize":"Click To Expand Code"};
/* ]]> */
</script>
<script type='text/javascript' src='http://www.santostang.com/wp-content/plugins/crayon-syntax-highlighter/js/min/crayon.min.js?ver=_2.7.2_beta'></script>
<script type='text/javascript' src='http://www.santostang.com/wp-includes/js/wp-embed.min.js?ver=4.7.9'></script>
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';        
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
</body>
</html>













<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>6v电影网，最新电影，最新电视剧，免费电影下载，电视剧下载，迅雷下载</title>
<meta name="keywords" content="最新电影下载,高清电影下载,最新电视剧下载" />
<meta name="description" content="6v电影（www.6vhao.tv），每天为广大网友搜集最新的电视剧和电影的资源下载，以及好看的电影、电视剧、综艺、动漫等迅雷下载，下载电影电视剧就上www.6vhao.tv。" />
<link href="/template/default1/images/style.css" rel="stylesheet" type="text/css" />
<script>var sitePath=''</script>
<script src="/js/common.js"></script>
<script src="/js/function.js"></script>
</head>
<body>
<div class="top"><div> <a href="http://www.6vhao.tv/jddy/2012-11-17/20441.html" target=_blank>[历年北美电影票房排行榜]</a> <a href="http://www.6vhao.tv/jddy/2018-01-21/33393.html" target=_blank>[豆瓣2017电影排行榜]</a>  <a href="http://www.6vhao.tv/zy/2016-05-22/29683.html" target=_blank>[历届奥斯卡最佳影片合集]</a> <a href="http://www.6vhao.tv/dy2/2015-06-13/27545.html" target=_blank>[30部无尿点电影]</a> <a href="http://www.6vhao.tv/jddy/2018-01-14/33347.html" target=_blank>[2017豆瓣热门电影集]</a> <a href="http://www.6vhao.tv/jddy/2013-08-04/22448.html" target=_blank>[全球十大经典剧情片]</a>  <a href="http://www.6vhao.tv/jddy/2013-12-03/23419.html" target=_blank>[保罗·沃克电影合集]</a> </div></div>
<DIV class="wrap">
  <DIV id=head_index>
    <!--头部-->
    <DIV id=header>
      <DIV id="left_header"><a href="http://www.6vhao.tv/" target="_blank" ><IMG src="/pic/logo.png"></a></DIV>
      <div class="ad"> <script src="/d/js/acmsd/w2.js"></script> </div>
          </DIV>
  </DIV>
  <DIV class=menutv>
    <UL>
      <LI><A href="http://www.6vhao.tv/" target="_self">首页</A> </LI>
      <li><a href="http://www.6vhao.tv/dy1/"[!--sel--]>喜剧片</a></li><li><a href="http://www.6vhao.tv/dy2/"[!--sel--]>动作片</a></li><li><a href="http://www.6vhao.tv/dy3/"[!--sel--]>爱情片</a></li><li><a href="http://www.6vhao.tv/dy5/"[!--sel--]>恐怖片</a></li><li><a href="http://www.6vhao.tv/dy6/"[!--sel--]>科幻片</a></li><li><a href="http://www.6vhao.tv/zzp/"[!--sel--]>战争片</a></li><li><a href="http://www.6vhao.tv/jlp/"[!--sel--]>纪录片</a></li><li><a href="http://www.6vhao.tv/jddy/"[!--sel--]>故事片</a></li><li><a href="http://www.6vhao.tv/dy4/"[!--sel--]>动画片</a></li><li><a href="http://www.6vhao.tv/dlz/"[!--sel--]>国剧</a></li><li><a href="http://www.6vhao.tv/rj/"[!--sel--]>日韩剧</a></li><li><a href="http://www.6vhao.tv/mj/"[!--sel--]>欧美剧</a></li><li><a href="http://www.6vhao.tv/3d/"[!--sel--]>3D电影</a></li><li><a href="http://www.6vhao.tv/zy/"[!--sel--]>综艺</a></li>    </UL>
  </DIV>
  <DIV id="search">
 
<form action="/e/search/index.php" method="post" name="searchform" id="searchform">
      <input type="hidden" name="show" value="title,smalltext" />
<input type="hidden" name="tempid" value="1" /><input type="hidden" name="tbname" value="Article" />
      <input type="text" name="keyboard" class="input_key"  value="支持模糊搜索，例如十月围城，可搜索十月"  onfocus="this.value='';"> 
      <INPUT class="button" name="submit" type="submit" value="">
     　　　<p><a class="hitbg" href="/hot.html"><font color="#000000">热播排行榜</font></a>　<a href="http://www.6vhao.tv/" target="_blank">在线观看</a>　　<a href="http://www.6vhao.tv/e/tool/gbook/?bid=2"  target="_blank" style="color:#418100;font-weight:bold; text-decoration:underline;">求片留言</a> <a href="http://www.6vhao.tv/help.html"  target="_blank" style="color:#418100;font-weight:bold; text-decoration:underline;">观看帮助</a>   <a onclick="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.6vhao.tv/');" href="#" style="color:#418100;font-weight:bold; text-decoration:underline;">设为首页</a></p>
      </FORM>
      <p class="keywords"><b>热门搜索：</b><a href='http://www.6vhao.tv/e/search/result/?searchid=184914' target=_blank>行尸走肉</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=185384' target=_blank>速度与激情</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=192342' target=_blank>战狼</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=185116' target=_blank>变形金刚</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=185246' target=_blank>权力的游戏</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=363678' target=_blank>鬼吹灯</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=319097' target=_blank>闪电侠</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=184972' target=_blank>生活大爆炸</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=184698' target=_blank>生化危机</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=248521' target=_blank>权利的游戏</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=184896' target=_blank>越狱</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=391114' target=_blank>老九门</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=285190' target=_blank>一路向西</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=186120' target=_blank>冰与火之歌</a>&nbsp;<a href='http://www.6vhao.tv/e/search/result/?searchid=185097' target=_blank>哈利波特</a><br></p>
  </DIV>
</DIV>
<div align="center"><script src="/d/js/acmsd/w3.js"></script><script src="/d/syt.js"></script></div>
<DIV class="wrap">
	<div class="tjlist">
		<h2>最新电影       【本站启用新地址www.6vhao.tv请大家收藏。】</h2>		<div class="clear"></div>
		<ul>			
            <li><a href="http://www.6vhao.tv/jddy/2018-02-02/33464.html" target="_blank"><img src="https://tu.66vod.net/2017/7764.jpg" title="华盛顿邮报"/><span></span></a><p><a href="http://www.6vhao.tv/jddy/2018-02-02/33464.html" title="华盛顿邮报" target="_blank">华盛顿邮报</a></p></li>
<li><a href="http://www.6vhao.tv/zzp/2018-04-04/33801.html" target="_blank"><img src="https://tu.66vod.net/2018/0299.jpg" title="12勇士"/><span></span></a><p><a href="http://www.6vhao.tv/zzp/2018-04-04/33801.html" title="12勇士" target="_blank">12勇士</a></p></li>
<li><a href="http://www.6vhao.tv/jddy/2018-04-03/33800.html" target="_blank"><img src="https://tu.66vod.net/2018/0289.jpg" title="芬兰的汤姆"/><span></span></a><p><a href="http://www.6vhao.tv/jddy/2018-04-03/33800.html" title="芬兰的汤姆" target="_blank">芬兰的汤姆</a></p></li>
<li><a href="http://www.6vhao.tv/dy6/2018-04-03/33799.html" target="_blank"><img src="https://tu.66vod.net/2018/0291.jpg" title="泰坦"/><span></span></a><p><a href="http://www.6vhao.tv/dy6/2018-04-03/33799.html" title="泰坦" target="_blank">泰坦</a></p></li>
<li><a href="http://www.6vhao.tv/jddy/2018-04-03/33798.html" target="_blank"><img src="https://tu.66vod.net/2018/0288.jpg" title="罗斯福先生"/><span></span></a><p><a href="http://www.6vhao.tv/jddy/2018-04-03/33798.html" title="罗斯福先生" target="_blank">罗斯福先生</a></p></li>
<li><a href="http://www.6vhao.tv/dy5/2018-04-03/33796.html" target="_blank"><img src="https://tu.66vod.net/2018/0275.jpg" title="侍女/女仆"/><span></span></a><p><a href="http://www.6vhao.tv/dy5/2018-04-03/33796.html" title="侍女/女仆" target="_blank">侍女/女仆</a></p></li>
<li><a href="http://www.6vhao.tv/dy5/2018-04-03/33795.html" target="_blank"><img src="https://tu.66vod.net/2018/0282.jpg" title="断魂小丑"/><span></span></a><p><a href="http://www.6vhao.tv/dy5/2018-04-03/33795.html" title="断魂小丑" target="_blank">断魂小丑</a></p></li>
<li><a href="http://www.6vhao.tv/jddy/2018-03-14/33666.html" target="_blank"><img src="https://tu.66vod.net/2017/8512.jpg" title="闺蜜2：无二不作"/><span></span></a><p><a href="http://www.6vhao.tv/jddy/2018-03-14/33666.html" title="闺蜜2：无二不作" target="_blank">闺蜜2：无二不作</a></p></li>
<li><a href="http://www.6vhao.tv/dy1/2018-04-03/33794.html" target="_blank"><img src="https://tu.66vod.net/2018/0283.jpg" title="无巧不成婚"/><span></span></a><p><a href="http://www.6vhao.tv/dy1/2018-04-03/33794.html" title="无巧不成婚" target="_blank">无巧不成婚</a></p></li>
<li><a href="http://www.6vhao.tv/jddy/2018-04-02/33790.html" target="_blank"><img src="https://tu.66vod.net/2018/0277.jpg" title="食人之饥"/><span></span></a><p><a href="http://www.6vhao.tv/jddy/2018-04-02/33790.html" title="食人之饥" target="_blank">食人之饥</a></p></li>
</ul>
	</div>
	<div class="tnlist">
		<h2><span><a href="/top.html" target="_blank" style="text-decoration:underline"><b>最新TOP50部</b></a></span>最新更新影片</h2>
		<div class="clear"></div>
		<ul><li><span >04-04</span><a href="http://www.6vhao.tv/jddy/2018-02-02/33464.html" target="_blank">华盛顿邮报</a></li>
<li><span >04-04</span><a href="http://www.6vhao.tv/zzp/2018-04-04/33801.html" target="_blank">12勇士</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/jddy/2018-04-03/33800.html" target="_blank">芬兰的汤姆</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/dy6/2018-04-03/33799.html" target="_blank">泰坦</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/jddy/2018-04-03/33798.html" target="_blank">罗斯福先生</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/dy5/2018-04-03/33796.html" target="_blank">侍女/女仆</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/dy5/2018-04-03/33795.html" target="_blank">断魂小丑</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/jddy/2018-03-14/33666.html" target="_blank">闺蜜2：无二不作</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/dy1/2018-04-03/33794.html" target="_blank">无巧不成婚</a></li>
<li><span >04-02</span><a href="http://www.6vhao.tv/jddy/2018-04-02/33790.html" target="_blank">食人之饥</a></li>
<li><span >04-02</span><a href="http://www.6vhao.tv/jddy/2018-04-02/33789.html" target="_blank">迷失的兄弟</a></li>
<li><span >04-02</span><a href="http://www.6vhao.tv/dy3/2018-04-02/33788.html" target="_blank">奶酪陷阱电影版</a></li>
<li><span >04-02</span><a href="http://www.6vhao.tv/dy2/2018-04-02/33787.html" target="_blank">玩命</a></li>
<li><span >04-02</span><a href="http://www.6vhao.tv/dy1/2018-04-02/33786.html" target="_blank">二麻租媳妇</a></li>
<li><span >04-02</span><a href="http://www.6vhao.tv/dy3/2018-04-02/33785.html" target="_blank">巴特克里克</a></li>
</ul>
	</div>
	<div class="blank_4px"></div>
</DIV>
<DIV class="wrap">
	<div class="tjlist">
		<h2>最新电视剧</h2>
		<div class="clear"></div>
		<ul><li><a href="http://www.6vhao.tv/mj/2018-03-27/33751.html" target="_blank"><img src="http://tu.66vod.net/2018/0164.jpg" title="极地恶灵[第一季03]"/><span></span></a><p><a href="http://www.6vhao.tv/mj/2018-03-27/33751.html" title="极地恶灵[第一季03]" target="_blank">极地恶灵[第一季0</a></p></li>
<li><a href="http://www.6vhao.tv/dlz/2018-03-06/33632.html" target="_blank"><img src="https://tu.66vod.net/2017/8410.jpg" title="果栏中的江湖大嫂"/><span></span></a><p><a href="http://www.6vhao.tv/dlz/2018-03-06/33632.html" title="果栏中的江湖大嫂" target="_blank">果栏中的江湖大嫂</a></p></li>
<li><a href="http://www.6vhao.tv/dlz/2018-04-03/33793.html" target="_blank"><img src="https://tu.66vod.net/2018/0281.jpg" title="逆缘"/><span></span></a><p><a href="http://www.6vhao.tv/dlz/2018-04-03/33793.html" title="逆缘" target="_blank">逆缘</a></p></li>
<li><a href="http://www.6vhao.tv/dlz/2017-02-22/31328.html" target="_blank"><img src="https://tu.66vod.net/2016/2968.jpg" title="爱回家之开心速递"/><span></span></a><p><a href="http://www.6vhao.tv/dlz/2017-02-22/31328.html" title="爱回家之开心速递" target="_blank">爱回家之开心速递</a></p></li>
<li><a href="http://www.6vhao.tv/dlz/2018-03-28/33753.html" target="_blank"><img src="https://tu.66vod.net/2018/0189.jpg" title="好久不见"/><span></span></a><p><a href="http://www.6vhao.tv/dlz/2018-03-28/33753.html" title="好久不见" target="_blank">好久不见</a></p></li>
<li><a href="http://www.6vhao.tv/dlz/2018-03-26/33743.html" target="_blank"><img src="https://tu.66vod.net/2018/0128.jpg" title="南方有乔木"/><span></span></a><p><a href="http://www.6vhao.tv/dlz/2018-03-26/33743.html" title="南方有乔木" target="_blank">南方有乔木</a></p></li>
<li><a href="http://www.6vhao.tv/mj/2018-03-31/33774.html" target="_blank"><img src="https://tu.66vod.net/2018/0239.jpg" title="雷蒙斯尼奇的不幸历险[第二季10]"/><span></span></a><p><a href="http://www.6vhao.tv/mj/2018-03-31/33774.html" title="雷蒙斯尼奇的不幸历险[第二季10]" target="_blank">雷蒙斯尼奇的不幸</a></p></li>
<li><a href="http://www.6vhao.tv/mj/2018-03-27/33750.html" target="_blank"><img src="http://tu.66vod.net/2018/0173.jpg" title="硅谷[第五季02]"/><span></span></a><p><a href="http://www.6vhao.tv/mj/2018-03-27/33750.html" title="硅谷[第五季02]" target="_blank">硅谷[第五季02]</a></p></li>
<li><a href="http://www.6vhao.tv/dlz/2018-04-03/33797.html" target="_blank"><img src="https://tu.66vod.net/2018/0271.jpg" title="远大前程[电视剧]"/><span></span></a><p><a href="http://www.6vhao.tv/dlz/2018-04-03/33797.html" title="远大前程[电视剧]" target="_blank">远大前程[电视剧]</a></p></li>
<li><a href="http://www.6vhao.tv/mj/2018-03-06/33634.html" target="_blank"><img src="https://tu.66vod.net/2017/8417.jpg" title="傲骨之战[第二季05]"/><span></span></a><p><a href="http://www.6vhao.tv/mj/2018-03-06/33634.html" title="傲骨之战[第二季05]" target="_blank">傲骨之战[第二季0</a></p></li>
</ul>
	</div>
	<div class="tnlist">
		<h2><span><a href="/hot.html" target="_blank" style="text-decoration:underline"><b>最新TOP50部</b></a></span>最新电视剧</h2>
		<div class="clear"></div>
		<ul><li><span >04-04</span><a href="http://www.6vhao.tv/mj/2018-03-27/33751.html" target="_blank">极地恶灵[第一季03]</a></li>
<li><span >04-04</span><a href="http://www.6vhao.tv/dlz/2018-03-06/33632.html" target="_blank">果栏中的江湖大嫂</a></li>
<li><span >04-04</span><a href="http://www.6vhao.tv/dlz/2018-04-03/33793.html" target="_blank">逆缘</a></li>
<li><span >04-04</span><a href="http://www.6vhao.tv/dlz/2017-02-22/31328.html" target="_blank">爱回家之开心速递</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/dlz/2018-03-28/33753.html" target="_blank">好久不见</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/dlz/2018-03-26/33743.html" target="_blank">南方有乔木</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/mj/2018-03-31/33774.html" target="_blank">雷蒙斯尼奇的不幸历险[第二季10]</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/mj/2018-03-27/33750.html" target="_blank">硅谷[第五季02]</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/dlz/2018-04-03/33797.html" target="_blank">远大前程[电视剧]</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/mj/2018-03-06/33634.html" target="_blank">傲骨之战[第二季05]</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/mj/2018-02-12/33520.html" target="_blank">国土安全[第七季08]</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/mj/2017-10-03/32751.html" target="_blank">最后一个男人[第四季13]</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/mj/2018-03-02/33607.html" target="_blank">鬼玩人之阿什斗厉鬼[第三季06]</a></li>
<li><span >04-03</span><a href="http://www.6vhao.tv/mj/2018-02-13/33526.html" target="_blank">此时此刻[第一季08]</a></li>
<li><span >04-02</span><a href="http://www.6vhao.tv/dlz/2018-03-06/33629.html" target="_blank">老男孩[全集]</a></li>
</ul>
	</div>
	<div class="blank_4px"></div>


<div id="gg300">
<div id="gd">
<ul>
<li><div id="net300l"><script src="http://www.6vhao.tv/d/3001.js"></script></div></li>
<li><div id="net300z"><script src="http://www.6vhao.tv/d/3002.js"></script></div></li>
<li><div id="net300r"><script src="http://www.6vhao.tv/d/3003.js"></script></div></li>
</ul>
</div>
</div>


  <div class="blank_4px"></div>
<div class="mainleft"> 
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/dy1/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/dy1/" target="_blank">喜剧片</a>(<bdo id="b67"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/dy1/2018-04-03/33794.html" title="无巧不成婚" target="_blank">无巧不成婚</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-04-02/33786.html" title="二麻租媳妇" target="_blank">二麻租媳妇</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-31/33778.html" title="布里斯比熊" target="_blank">布里斯比熊</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-28/33754.html" title="小鬼警察2：新兵" target="_blank">小鬼警察2：新兵</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-02-25/33587.html" title="祖宗十九代" target="_blank">祖宗十九代</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-24/33733.html" title="你完蛋了，老铁" target="_blank">你完蛋了，老铁</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-24/33726.html" title="宫合" target="_blank">宫合</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-23/33724.html" title="金装少年唐伯虎" target="_blank">金装少年唐伯虎</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-23/33723.html" title="疯狂熊孩子" target="_blank">疯狂熊孩子</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2016-08-13/30192.html" title="快手枪手快枪手" target="_blank">快手枪手快枪手</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2015-10-03/28296.html" title="小萝莉的猴神大叔" target="_blank">小萝莉的猴神大叔</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-21/33705.html" title="红衣女郎" target="_blank">红衣女郎</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-05/33626.html" title="帕丁顿熊2" target="_blank">帕丁顿熊2</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2018-03-16/33675.html" title="齐天大圣·万妖之城" target="_blank">齐天大圣·万妖之</a></li>
       
       <li><a href="http://www.6vhao.tv/dy1/2017-01-19/31115.html" title="呆呆计划" target="_blank">呆呆计划</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/dy2/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/dy2/" target="_blank">动作片</a>(<bdo id="b68"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/dy2/2018-04-02/33787.html" title="玩命" target="_blank">玩命</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-04-02/33784.html" title="特洛伊奥德赛" target="_blank">特洛伊奥德赛</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-03-31/33772.html" title="通勤营救" target="_blank">通勤营救</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-03-29/33761.html" title="速度与激战" target="_blank">速度与激战</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-03-29/33758.html" title="史前超人" target="_blank">史前超人</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-01-31/33449.html" title="移动迷宫3：死亡解药" target="_blank">移动迷宫3：死亡解</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2011-12-14/17136.html" title="古墓丽影1[高清]" target="_blank">古墓丽影1[高清]</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-03-25/33735.html" title="骄傲的玛丽" target="_blank">骄傲的玛丽</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2017-08-30/32512.html" title="破·局" target="_blank">破·局</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-02-26/33593.html" title="谜巢" target="_blank">谜巢</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-03-22/33713.html" title="亚瑟王和圆桌骑士" target="_blank">亚瑟王和圆桌骑士</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2017-12-24/qmdj.html" title="奇门遁甲2017" target="_blank">奇门遁甲2017</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-01-21/33390.html" title="维京：王者之战" target="_blank">维京：王者之战</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2018-03-18/33695.html" title="古墓丽影：源起之战" target="_blank">古墓丽影：源起之</a></li>
       
       <li><a href="http://www.6vhao.tv/dy2/2017-11-16/33013.html" title="神偷联盟" target="_blank">神偷联盟</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/dy3/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/dy3/" target="_blank">爱情片</a>(<bdo id="b69"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/dy3/2018-04-02/33788.html" title="奶酪陷阱电影版" target="_blank">奶酪陷阱电影版</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-04-02/33785.html" title="巴特克里克" target="_blank">巴特克里克</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-03-29/33755.html" title="时空偷渡少女" target="_blank">时空偷渡少女</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-02-12/33522.html" title="南极之恋" target="_blank">南极之恋</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-03-21/33709.html" title="恋爱禁止的世界" target="_blank">恋爱禁止的世界</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-03-17/33682.html" title="伊斯梅尔的幽魂" target="_blank">伊斯梅尔的幽魂</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-02-25/33584.html" title="西游记女儿国" target="_blank">西游记女儿国</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-01-01/33266.html" title="昼颜 电影版" target="_blank">昼颜 电影版</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-03-12/33657.html" title="第二个夏天，不再遇见的你" target="_blank">第二个夏天，不再</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-03-07/33637.html" title="准许" target="_blank">准许</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2014-02-25/24187.html" title="前任攻略" target="_blank">前任攻略</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-01-08/33305.html" title="前任3：再见前任" target="_blank">前任3：再见前任</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-03-02/33614.html" title="识色，幸也" target="_blank">识色，幸也</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-02-18/33554.html" title="4年，2男，1爱情" target="_blank">4年，2男，1爱情</a></li>
       
       <li><a href="http://www.6vhao.tv/dy3/2018-02-17/33552.html" title="顺德人家之合家欢" target="_blank">顺德人家之合家欢</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/dy5/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/dy5/" target="_blank">恐怖片</a>(<bdo id="b71"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/dy5/2018-04-03/33796.html" title="侍女/女仆" target="_blank">侍女/女仆</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-04-03/33795.html" title="断魂小丑" target="_blank">断魂小丑</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-31/33777.html" title="房客" target="_blank">房客</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-31/33776.html" title="玉米地的小孩:大逃亡" target="_blank">玉米地的小孩:大逃</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-29/33762.html" title="杂交种" target="_blank">杂交种</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2017-12-27/33237.html" title="韦罗妮卡" target="_blank">韦罗妮卡</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-28/33752.html" title="罗伯特的复仇" target="_blank">罗伯特的复仇</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-27/33748.html" title="黑暗缪斯" target="_blank">黑暗缪斯</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-25/33738.html" title="马柔本宅秘事" target="_blank">马柔本宅秘事</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-22/33710.html" title="潜伏1-4" target="_blank">潜伏1-4</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-02-08/33490.html" title="行监坐守" target="_blank">行监坐守</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-20/33703.html" title="头颅游戏" target="_blank">头颅游戏</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-18/33687.html" title="午夜人魔" target="_blank">午夜人魔</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-17/33680.html" title="我的小卷毛" target="_blank">我的小卷毛</a></li>
       
       <li><a href="http://www.6vhao.tv/dy5/2018-03-16/33678.html" title="南部僵尸来袭" target="_blank">南部僵尸来袭</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/dy6/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/dy6/" target="_blank">科幻片</a>(<bdo id="b72"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/dy6/2018-04-03/33799.html" title="泰坦" target="_blank">泰坦</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-04-01/33779.html" title="环太平洋2：雷霆再起" target="_blank">环太平洋2：雷霆再</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-03-29/33763.html" title="念力" target="_blank">念力</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-03-21/33708.html" title="预兆" target="_blank">预兆</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-03-16/33676.html" title="黑豹" target="_blank">黑豹</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2014-04-29/24740.html" title="天崩地裂" target="_blank">天崩地裂</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2017-12-28/33244.html" title="星球大战8：最后的绝地武士" target="_blank">星球大战8：最后的</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-03-12/33659.html" title="湮灭" target="_blank">湮灭</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-03-12/33658.html" title="冰肤传说" target="_blank">冰肤传说</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2017-05-31/31929.html" title="异星觉醒" target="_blank">异星觉醒</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2017-12-08/33138.html" title="正义联盟" target="_blank">正义联盟</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-03-01/33603.html" title="太平洋战场" target="_blank">太平洋战场</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-02-24/33581.html" title="静音" target="_blank">静音</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-02-23/33580.html" title="云端" target="_blank">云端</a></li>
       
       <li><a href="http://www.6vhao.tv/dy6/2018-02-19/33561.html" title="网关" target="_blank">网关</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/zzp/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/zzp/" target="_blank">战争片</a>(<bdo id="b73"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/zzp/2018-04-04/33801.html" title="12勇士" target="_blank">12勇士</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2018-03-15/33673.html" title="天上再见" target="_blank">天上再见</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2018-03-04/33621.html" title="冬季战争" target="_blank">冬季战争</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2018-03-04/33620.html" title="玩世英雄2018" target="_blank">玩世英雄2018</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2009-04-14/6712.html" title="帝国的毁灭[高清]" target="_blank">帝国的毁灭[高清]</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2018-01-28/33435.html" title="无问西东" target="_blank">无问西东</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2018-01-08/33309.html" title="龙之战" target="_blank">龙之战</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2018-01-08/33308.html" title="高山下的花环" target="_blank">高山下的花环</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2017-12-11/33156.html" title="敦刻尔克[国语]" target="_blank">敦刻尔克[国语]</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2017-09-15/32628.html" title="敦刻尔克" target="_blank">敦刻尔克</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2017-12-08/33137.html" title="血战湘江" target="_blank">血战湘江</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2017-10-23/32873.html" title="战俘的逃亡日记" target="_blank">战俘的逃亡日记</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2017-10-23/32870.html" title="巴黎血色围城" target="_blank">巴黎血色围城</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2017-10-13/32811.html" title="刺杀盖世太保" target="_blank">刺杀盖世太保</a></li>
       
       <li><a href="http://www.6vhao.tv/zzp/2017-08-02/32343.html" title="明月几时有" target="_blank">明月几时有</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/jlp/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/jlp/" target="_blank">纪录片</a>(<bdo id="b74"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-29/33760.html" title="我只认识你" target="_blank">我只认识你</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-26/33741.html" title="生门[全集]" target="_blank">生门[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-25/33739.html" title="源味中国" target="_blank">源味中国</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-19/33698.html" title="强岛" target="_blank">强岛</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-18/33690.html" title="火力全开" target="_blank">火力全开</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-17/33686.html" title="辉煌中国" target="_blank">辉煌中国</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-14/33664.html" title="成为邦德" target="_blank">成为邦德</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-10/33651.html" title="天梯：蔡国强的艺术" target="_blank">天梯：蔡国强的艺</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-08/33645.html" title="二十二" target="_blank">二十二</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-05/33625.html" title="拟音" target="_blank">拟音</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-03-01/33602.html" title="水果传" target="_blank">水果传</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-02-20/33562.html" title="舌尖上的中国3" target="_blank">舌尖上的中国3</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-02-20/33563.html" title="假如动物会摄影" target="_blank">假如动物会摄影</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-02-05/33479.html" title="小企鹅大长征2" target="_blank">小企鹅大长征2</a></li>
       
       <li><a href="http://www.6vhao.tv/jlp/2018-01-29/33436.html" title="火星世代" target="_blank">火星世代</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/jddy/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/jddy/" target="_blank">故事片</a>(<bdo id="b35"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/jddy/2018-02-02/33464.html" title="华盛顿邮报" target="_blank">华盛顿邮报</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-04-03/33800.html" title="芬兰的汤姆" target="_blank">芬兰的汤姆</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-04-03/33798.html" title="罗斯福先生" target="_blank">罗斯福先生</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-03-14/33666.html" title="闺蜜2：无二不作" target="_blank">闺蜜2：无二不作</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-04-02/33790.html" title="食人之饥" target="_blank">食人之饥</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-04-02/33789.html" title="迷失的兄弟" target="_blank">迷失的兄弟</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-04-01/33782.html" title="揭幕战" target="_blank">揭幕战</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-04-01/33781.html" title="猎鸟" target="_blank">猎鸟</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-04-01/33780.html" title="2018年03月佳片推荐" target="_blank">2018年03月佳片推</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-02-16/33544.html" title="与神同行" target="_blank">与神同行</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-03-31/33771.html" title="心灵想要大声呼喊[真人版]" target="_blank">心灵想要大声呼喊</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-03-30/33770.html" title="门" target="_blank">门</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-02-17/33547.html" title="大佛普拉斯" target="_blank">大佛普拉斯</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-03-29/33759.html" title="校花与野出租" target="_blank">校花与野出租</a></li>
       
       <li><a href="http://www.6vhao.tv/jddy/2018-03-29/33757.html" title="棋手" target="_blank">棋手</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/dy4/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/dy4/" target="_blank">动画片</a>(<bdo id="b70"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-30/33769.html" title="魔法总动员" target="_blank">魔法总动员</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-30/33768.html" title="大世界/好极了" target="_blank">大世界/好极了</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-27/33749.html" title="玛丽与魔女之花" target="_blank">玛丽与魔女之花</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-01-22/33398.html" title="哥斯拉：怪兽行星" target="_blank">哥斯拉：怪兽行星</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-15/33669.html" title="我的邻居山田君" target="_blank">我的邻居山田君</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2017-10-17/32830.html" title="乐高幻影忍者大电影" target="_blank">乐高幻影忍者大电</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-01-16/33364.html" title="宣告黎明的露之歌" target="_blank">宣告黎明的露之歌</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-12/33656.html" title="姆明与冬日仙境" target="_blank">姆明与冬日仙境</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-10/33650.html" title="金龟子" target="_blank">金龟子</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-06/33630.html" title="大坏狐狸的故事" target="_blank">大坏狐狸的故事</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-05/33622.html" title="巧克力与香子兰" target="_blank">巧克力与香子兰</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-03/33617.html" title="圣诞星" target="_blank">圣诞星</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-02-25/33585.html" title="公牛历险记" target="_blank">公牛历险记</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-02/33612.html" title="魔法科高校的劣等生呼唤星辰的少女" target="_blank">魔法科高校的劣等</a></li>
       
       <li><a href="http://www.6vhao.tv/dy4/2018-03-02/33611.html" title="游戏人生ZERO" target="_blank">游戏人生ZERO</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/dlz/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/dlz/" target="_blank">国剧</a>(<bdo id="b36"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-06/33632.html" title="果栏中的江湖大嫂" target="_blank">果栏中的江湖大嫂</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-04-03/33793.html" title="逆缘" target="_blank">逆缘</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2017-02-22/31328.html" title="爱回家之开心速递" target="_blank">爱回家之开心速递</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-28/33753.html" title="好久不见" target="_blank">好久不见</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-26/33743.html" title="南方有乔木" target="_blank">南方有乔木</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-04-03/33797.html" title="远大前程[电视剧]" target="_blank">远大前程[电视剧]</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-06/33629.html" title="老男孩[全集]" target="_blank">老男孩[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-02-19/33558.html" title="三个女人一个「因」" target="_blank">三个女人一个「因</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-07/33635.html" title="人生若如初相见" target="_blank">人生若如初相见</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-31/33773.html" title="动物系恋人啊" target="_blank">动物系恋人啊</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-06/33627.html" title="烈火如歌" target="_blank">烈火如歌</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-06/33631.html" title="翻生武林[全集]" target="_blank">翻生武林[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-15/33672.html" title="万能图书馆" target="_blank">万能图书馆</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-03-29/33764.html" title="三国机密之潜龙在渊" target="_blank">三国机密之潜龙在</a></li>
       
       <li><a href="http://www.6vhao.tv/dlz/2018-02-02/33458.html" title="蜀山战纪2踏火行歌" target="_blank">蜀山战纪2踏火行歌</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/rj/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/rj/" target="_blank">日韩剧</a>(<bdo id="b60"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/rj/2018-04-02/33791.html" title="经常请吃饭的漂亮姐姐" target="_blank">经常请吃饭的漂亮</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-03-19/33700.html" title="Live" target="_blank">Live</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-01-24/33416.html" title="电影少女～VIDEO GIRL AI 2018～[全集]" target="_blank">电影少女～VIDEO </a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-03-30/33767.html" title="我的大叔" target="_blank">我的大叔</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-03-22/33712.html" title="[日剧]记忆" target="_blank">[日剧]记忆</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2017-10-27/32897.html" title="黑色五叶草[全集]" target="_blank">黑色五叶草[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2017-10-25/32882.html" title="小松先生[全集]" target="_blank">小松先生[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-02-18/33556.html" title="迷雾[全集]" target="_blank">迷雾[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-01-24/33415.html" title="OH MY JUMP！ ～少年JUMP拯救地球～[全集]" target="_blank">OH MY JUMP！ ～少</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2017-10-21/32855.html" title="魔法使的新娘[全集]" target="_blank">魔法使的新娘[全集</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-01-26/33426.html" title="anone[全集]" target="_blank">anone[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-01-24/33413.html" title="邻家月更圆[全集]" target="_blank">邻家月更圆[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-01-24/33409.html" title="海月姬[全集]" target="_blank">海月姬[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2017-10-25/32884.html" title="相棒16[全集]" target="_blank">相棒16[全集]</a></li>
       
       <li><a href="http://www.6vhao.tv/rj/2018-01-24/33410.html" title="99.9：刑事专业律师2[全集]" target="_blank">99.9：刑事专业律</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/mj/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/mj/" target="_blank">欧美剧</a>(<bdo id="b61"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/mj/2018-03-27/33751.html" title="极地恶灵[第一季03]" target="_blank">极地恶灵[第一季0</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-03-31/33774.html" title="雷蒙斯尼奇的不幸历险[第二季10]" target="_blank">雷蒙斯尼奇的不幸</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-03-27/33750.html" title="硅谷[第五季02]" target="_blank">硅谷[第五季02]</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-03-06/33634.html" title="傲骨之战[第二季05]" target="_blank">傲骨之战[第二季0</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-02-12/33520.html" title="国土安全[第七季08]" target="_blank">国土安全[第七季0</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2017-10-03/32751.html" title="最后一个男人[第四季13]" target="_blank">最后一个男人[第四</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-03-02/33607.html" title="鬼玩人之阿什斗厉鬼[第三季06]" target="_blank">鬼玩人之阿什斗厉</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-02-13/33526.html" title="此时此刻[第一季08]" target="_blank">此时此刻[第一季0</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2017-10-23/32869.html" title="行尸走肉[第八季14]" target="_blank">行尸走肉[第八季1</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-04-02/33792.html" title="无妄之灾[第一季01]" target="_blank">无妄之灾[第一季0</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-03-31/33775.html" title="诡媚海妖[第一季02]" target="_blank">诡媚海妖[第一季0</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2018-04-02/33783.html" title="男孩们的冒险书[第一季01]" target="_blank">男孩们的冒险书[第</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2017-10-08/32774.html" title="童话镇[第七季15]" target="_blank">童话镇[第七季15]</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2017-10-01/32736.html" title="天堂执法者[第八季18]" target="_blank">天堂执法者[第八季</a></li>
       
       <li><a href="http://www.6vhao.tv/mj/2017-10-29/32907.html" title="盲点[第三季17]" target="_blank">盲点[第三季17]</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/3d/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/3d/" target="_blank">3D电影</a>(<bdo id="b75"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/3d/2018-03-08/33643.html" title="雷神3[左右3D版]" target="_blank">雷神3[左右3D版]</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2018-03-08/33642.html" title="莫斯科陷落[左右3D版]" target="_blank">莫斯科陷落[左右3</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2018-03-08/33641.html" title="寻梦环游记[左右3D版]" target="_blank">寻梦环游记[左右3</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2018-03-08/33640.html" title="正义联盟[左右3D版]" target="_blank">正义联盟[左右3D版</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2018-01-23/33404.html" title="银翼杀手2049[左右3D版]" target="_blank">银翼杀手2049[左右</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2018-01-23/33403.html" title="全球风暴[左右3D版]" target="_blank">全球风暴[左右3D版</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2018-01-23/33402.html" title="乐高幻影忍者大电影[左右3D版]" target="_blank">乐高幻影忍者大电</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-12-07/33131.html" title="冰雪女王3:火与冰[左右3D版]" target="_blank">冰雪女王3:火与冰</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-12-07/33130.html" title="终结者2:审判日[左右3D版]" target="_blank">终结者2:审判日[左</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-12-07/33129.html" title="星际特工:千星之城[左右3D版]" target="_blank">星际特工:千星之城</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-11-10/32972.html" title="赛车总动员3:极速挑战[左右3D版]" target="_blank">赛车总动员3:极速</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-10-30/32915.html" title="神偷奶爸3[左右3D版]" target="_blank">神偷奶爸3[左右3D</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-10-30/32914.html" title="变形金刚5[左右3D版]" target="_blank">变形金刚5[左右3D</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-10-30/32913.html" title="勇士之门[左右3D版]" target="_blank">勇士之门[左右3D版</a></li>
       
       <li><a href="http://www.6vhao.tv/3d/2017-10-30/32912.html" title="猩球崛起3：终极之战[左右3D版]" target="_blank">猩球崛起3：终极之</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		<div class="channeltype">
			<h2><span><a href="http://www.6vhao.tv/zy/" target="_blank">更多影片>></a></span><a href="http://www.6vhao.tv/zy/" target="_blank">综艺</a>(<bdo id="b62"></bdo>部)</h2>
			<div class="clear"></div>
			<ul>
				       
       <li><a href="http://www.6vhao.tv/zy/2018-03-11/33654.html" title="第90届奥斯卡颁奖典礼" target="_blank">第90届奥斯卡颁奖</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2018-02-22/33574.html" title="2018央视春晚会" target="_blank">2018央视春晚会</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2018-02-02/33461.html" title="第60届格莱美颁奖典礼" target="_blank">第60届格莱美颁奖</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-12-13/33169.html" title="汪峰2017岁月巡回演唱会深圳站" target="_blank">汪峰2017岁月巡回</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-11-30/33082.html" title="维多利亚的秘密时尚内衣秀2017" target="_blank">维多利亚的秘密时</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-11-23/33050.html" title="第45届全美音乐大奖" target="_blank">第45届全美音乐大</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-09-12/32606.html" title="汪峰2017岁月巡回演唱会北京站" target="_blank">汪峰2017岁月巡回</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-08-17/32424.html" title="TFBOYS四周年演唱会" target="_blank">TFBOYS四周年演唱</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-05-04/31748.html" title="卢冠廷Beyond Imagination演唱会" target="_blank">卢冠廷Beyond Ima</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-04-25/31698.html" title="李宗盛：既然青春留不住" target="_blank">李宗盛：既然青春</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-03-21/31506.html" title="郑秀文Touch Mi 2演唱会" target="_blank">郑秀文Touch Mi 2</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-03-10/31438.html" title="机器男友" target="_blank">机器男友</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-03-10/31437.html" title="德云社丁酉年开箱庆典" target="_blank">德云社丁酉年开箱</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-02-27/31363.html" title="第89届奥斯卡金像奖" target="_blank">第89届奥斯卡金像</a></li>
       
       <li><a href="http://www.6vhao.tv/zy/2017-02-03/31216.html" title="2017天津卫视春晚" target="_blank">2017天津卫视春晚</a></li>
       
				
			</ul>
			<div class="blank_4px"></div>
		</div>
		<div class="blank_5px"></div>
		        
<span id=span_b67>3120</span>
<script language=Javascript>
document.getElementById("b67").innerHTML=document.getElementById("span_b67").innerHTML;
document.getElementById("span_b67").innerHTML="";
</script>

<span id=span_b68>4210</span>
<script language=Javascript>
document.getElementById("b68").innerHTML=document.getElementById("span_b68").innerHTML;
document.getElementById("span_b68").innerHTML="";
</script>

<span id=span_b69>2439</span>
<script language=Javascript>
document.getElementById("b69").innerHTML=document.getElementById("span_b69").innerHTML;
document.getElementById("span_b69").innerHTML="";
</script>

<span id=span_b71>2187</span>
<script language=Javascript>
document.getElementById("b71").innerHTML=document.getElementById("span_b71").innerHTML;
document.getElementById("span_b71").innerHTML="";
</script>

<span id=span_b72>1388</span>
<script language=Javascript>
document.getElementById("b72").innerHTML=document.getElementById("span_b72").innerHTML;
document.getElementById("span_b72").innerHTML="";
</script>

<span id=span_b73>566</span>
<script language=Javascript>
document.getElementById("b73").innerHTML=document.getElementById("span_b73").innerHTML;
document.getElementById("span_b73").innerHTML="";
</script>

<span id=span_b74>527</span>
<script language=Javascript>
document.getElementById("b74").innerHTML=document.getElementById("span_b74").innerHTML;
document.getElementById("span_b74").innerHTML="";
</script>

<span id=span_b35>5932</span>
<script language=Javascript>
document.getElementById("b35").innerHTML=document.getElementById("span_b35").innerHTML;
document.getElementById("span_b35").innerHTML="";
</script>

<span id=span_b70>1483</span>
<script language=Javascript>
document.getElementById("b70").innerHTML=document.getElementById("span_b70").innerHTML;
document.getElementById("span_b70").innerHTML="";
</script>

<span id=span_b36>2279</span>
<script language=Javascript>
document.getElementById("b36").innerHTML=document.getElementById("span_b36").innerHTML;
document.getElementById("span_b36").innerHTML="";
</script>

<span id=span_b60>932</span>
<script language=Javascript>
document.getElementById("b60").innerHTML=document.getElementById("span_b60").innerHTML;
document.getElementById("span_b60").innerHTML="";
</script>

<span id=span_b61>1802</span>
<script language=Javascript>
document.getElementById("b61").innerHTML=document.getElementById("span_b61").innerHTML;
document.getElementById("span_b61").innerHTML="";
</script>

<span id=span_b75>350</span>
<script language=Javascript>
document.getElementById("b75").innerHTML=document.getElementById("span_b75").innerHTML;
document.getElementById("span_b75").innerHTML="";
</script>

<span id=span_b62>523</span>
<script language=Javascript>
document.getElementById("b62").innerHTML=document.getElementById("span_b62").innerHTML;
document.getElementById("span_b62").innerHTML="";
</script>
		 </div>
	<div class="mainright">
		<div class="listhit">
			<h2>2018观看排行榜</h2>
			<div class="clear"></div>
			<ul>
				<li><span>12-12</span><a href="http://www.6vhao.tv/mj/2017-07-17/32235.html" target="_blank">权力的游戏[第七季全]</a></li>
<li><span>01-07</span><a href="http://www.6vhao.tv/dy2/2017-07-27/32311.html" target="_blank">绣春刀II：修罗战场</a></li>
<li><span>09-23</span><a href="http://www.6vhao.tv/dy6/2017-07-03/32129.html" target="_blank">变形金刚5：最后的骑士</a></li>
<li><span>10-15</span><a href="http://www.6vhao.tv/dy4/2017-07-12/32200.html" target="_blank">神偷奶爸3</a></li>
<li><span>02-17</span><a href="http://www.6vhao.tv/dy6/2017-07-30/32330.html" target="_blank">逆时营救</a></li>
<li><span>01-17</span><a href="http://www.6vhao.tv/jddy/2017-03-27/buju.html" target="_blank">看不见的客人</a></li>
<li><span>11-04</span><a href="http://www.6vhao.tv/dy2/2017-07-06/32143.html" target="_blank">恶女</a></li>
<li><span>09-16</span><a href="http://www.6vhao.tv/dy3/2017-07-07/32148.html" target="_blank">原谅他77次</a></li>
<li><span>09-19</span><a href="http://www.6vhao.tv/mj/2017-07-17/32239.html" target="_blank">血族[第四季全]</a></li>
<li><span>09-23</span><a href="http://www.6vhao.tv/dy1/2017-07-27/32309.html" target="_blank">喵星人</a></li>
<li><span>09-23</span><a href="http://www.6vhao.tv/mj/2016-06-29/29941.html" target="_blank">困兽[第三季13]</a></li>
<li><span>01-31</span><a href="http://www.6vhao.tv/dy6/2015-05-24/27382.html" target="_blank">复仇者联盟2：奥创纪元</a></li>
<li><span>10-01</span><a href="http://www.6vhao.tv/dy4/2017-05-21/31851.html" target="_blank">在这世界的角落</a></li>
<li><span>09-17</span><a href="http://www.6vhao.tv/jddy/2017-07-02/32124.html" target="_blank">绝命时钟</a></li>
<li><span>09-18</span><a href="http://www.6vhao.tv/rj/2017-07-16/32225.html" target="_blank">侦探物语[全集]</a></li>
<li><span>01-02</span><a href="http://www.6vhao.tv/dy2/2017-07-22/32279.html" target="_blank">真实</a></li>
<li><span>11-26</span><a href="http://www.6vhao.tv/jddy/2017-07-22/32283.html" target="_blank">一念无明</a></li>
<li><span>12-23</span><a href="http://www.6vhao.tv/dy4/2017-07-24/32293.html" target="_blank">刀剑神域：序列之争剧场版</a></li>
<li><span>09-26</span><a href="http://www.6vhao.tv/mj/2017-07-25/32300.html" target="_blank">球手[第三季10]</a></li>
<li><span>03-15</span><a href="http://www.6vhao.tv/jddy/2011-05-22/14897.html" target="_blank">跛豪BD高清</a></li>
<li><span>03-15</span><a href="http://www.6vhao.tv/dy6/2014-04-29/24740.html" target="_blank">天崩地裂</a></li>
<li><span>02-02</span><a href="http://www.6vhao.tv/jddy/2011-04-17/14569.html" target="_blank">荒岛余生[高清]</a></li>
<li><span>02-03</span><a href="http://www.6vhao.tv/jddy/2018-02-03/33466.html" target="_blank">咖啡风暴</a></li>
<li><span>02-09</span><a href="http://www.6vhao.tv/zzp/2009-04-14/6712.html" target="_blank">帝国的毁灭[高清]</a></li>
<li><span>09-19</span><a href="http://www.6vhao.tv/dy3/2010-02-04/10177.html" target="_blank">我的爱在我身边[高清]</a></li>
<li><span>11-15</span><a href="http://www.6vhao.tv/dlz/2011-09-11/16026.html" target="_blank">步步惊心[全集]</a></li>
<li><span>01-23</span><a href="http://www.6vhao.tv/dy2/2011-10-12/16422.html" target="_blank">国家宝藏1[高清]</a></li>
<li><span>02-02</span><a href="http://www.6vhao.tv/dy1/2018-01-23/33401.html" target="_blank">迷镇凶案</a></li>
<li><span>01-23</span><a href="http://www.6vhao.tv/dy2/2011-10-12/16423.html" target="_blank">国家宝藏2[高清]</a></li>
			</ul>
			<div class="clear"></div>
		</div>
		<div class="blank_4px"></div>
		<div class="listhit">
			<h2>本周观看排行榜</h2>
			<div class="clear"></div>
			<ul><li><span>04-04</span><a href="http://www.6vhao.tv/dlz/2017-02-22/31328.html" target="_blank">爱回家之开心速递</a></li>
<li><span>03-27</span><a href="http://www.6vhao.tv/jddy/2017-08-04/32346.html" target="_blank">龙顺</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-22/32667.html" target="_blank">哥谭[第四季16]</a></li>
<li><span>03-29</span><a href="http://www.6vhao.tv/mj/2017-09-27/32701.html" target="_blank">衰女翻身[第二季19]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-26/32690.html" target="_blank">生活大爆炸[第十一季18]</a></li>
<li><span>03-28</span><a href="http://www.6vhao.tv/mj/2017-09-26/32694.html" target="_blank">等待夕阳好[第二季20]</a></li>
<li><span>03-28</span><a href="http://www.6vhao.tv/mj/2017-09-26/32695.html" target="_blank">天蝎[第四季20]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-26/32696.html" target="_blank">少年谢尔顿[第一季16]</a></li>
<li><span>03-28</span><a href="http://www.6vhao.tv/mj/2017-09-27/32697.html" target="_blank">仁医[第一季18]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-28/32705.html" target="_blank">摩登家庭[第九季17]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-29/32708.html" target="_blank">海豹突击队[第一季17]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-29/32709.html" target="_blank">金色年代[第五季17]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-29/32710.html" target="_blank">嘻哈帝国[第四季10]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-29/32712.html" target="_blank">犯罪心理[第十三季18]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-09-29/32714.html" target="_blank">指定幸存者[第二季15]</a></li>
<li><span>03-31</span><a href="http://www.6vhao.tv/mj/2017-09-30/32727.html" target="_blank">芝加哥烈焰[第六季16]</a></li>
<li><span>04-01</span><a href="http://www.6vhao.tv/mj/2017-10-01/32736.html" target="_blank">天堂执法者[第八季18]</a></li>
<li><span>03-31</span><a href="http://www.6vhao.tv/mj/2017-10-01/32738.html" target="_blank">新百战天龙[第二季18]</a></li>
<li><span>04-03</span><a href="http://www.6vhao.tv/mj/2017-10-03/32751.html" target="_blank">最后一个男人[第四季13]</a></li>
<li><span>04-02</span><a href="http://www.6vhao.tv/mj/2017-10-08/32774.html" target="_blank">童话镇[第七季15]</a></li>
<li><span>03-28</span><a href="http://www.6vhao.tv/mj/2017-10-12/32803.html" target="_blank">明日传奇[第三季16]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-10-13/32808.html" target="_blank">河谷镇[第二季17]</a></li>
<li><span>03-31</span><a href="http://www.6vhao.tv/mj/2017-10-14/32817.html" target="_blank">绿箭[第六季16]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-10-15/32822.html" target="_blank">国务卿女士[第四季15]</a></li>
<li><span>04-02</span><a href="http://www.6vhao.tv/mj/2017-10-23/32869.html" target="_blank">行尸走肉[第八季14]</a></li>
<li><span>03-27</span><a href="http://www.6vhao.tv/rj/2017-10-25/32882.html" target="_blank">小松先生[全集]</a></li>
<li><span>03-28</span><a href="http://www.6vhao.tv/rj/2017-10-27/32897.html" target="_blank">黑色五叶草[全集]</a></li>
<li><span>04-01</span><a href="http://www.6vhao.tv/mj/2017-10-29/32907.html" target="_blank">盲点[第三季17]</a></li>
<li><span>03-30</span><a href="http://www.6vhao.tv/mj/2017-11-03/32935.html" target="_blank">极品老妈[第五季15]</a></li>
<li><span>03-29</span><a href="http://www.6vhao.tv/mj/2017-11-23/33046.html" target="_blank">芝加哥医院[第三季13]</a></li>
</ul><div class="blank_4px blank_3px"></div>
		</div>
        <div class="blank_4px"></div>
	</div>
	<div class="clear">  </div>	<div class="linklist">
		<h2>友情链接：要求Alexa排名20W以内,百度权限相同,做连接的请发邮件.</h2>
		<ul>			
			<table width=100% border=0 cellpadding=3 cellspacing=0><tr><td align=center><a href='http://www.dygang.net' title='电影港' target=_blank>电影港</a></td><td align=center><a href='http://www.6vhao.tv/mj/' title='最新美剧' target=_blank>最新美剧</a></td><td align=center><a href='http://www.pp63.com/dy/' title='最新电影' target=_blank>最新电影</a></td><td align=center><a href='http://www.baidu.com' title='百度baidu' target=_blank>百度baidu</a></td><td></td><td></td></tr></table>		</ul>
		<div class="blank_4px"></div>  
</div><div class="searlefth1"> <li>  </li> </div> 
<div id="footer"> 6V电影-最给力的电影网-提供最新电影,最新电视剧,免费电影迅雷下载<p>本站资源来自互联网免费共享,仅供交流学习之用,版权归作者本人所有,如果侵犯了您的权益,请通知我们。<p>
<div style='display:none'>
<script src=/d/tj.js></script>
</div>| 苏ICP备11026244号 | 管理员信箱：6vhaonet#gmail.com | <a href="http://www.6vhao.tv/" target="_blank">6vhao.tv</a>|</div></body>
</html>