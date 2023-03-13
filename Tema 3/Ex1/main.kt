package ro.mike.tuiasi

import org.jsoup.Jsoup;

data class Rss(
    val title: String,
    val link: String,
    val desc: String,
    val item: List<RssItem>
){}

data class RssItem(
    val title: String,
    val link: String,
    val desc: String,
    val pubDate: String
){}

fun main(args: Array<String>){
    val doc = Jsoup.connect("http://rss.cnn.com/rss/edition.rss").get();
    val rssItem = doc.select("item").map{
        val title = it.select("title").text()
        val link = it.select("link").text()
        val description = it.select("description").text()
        val pubDate = it.select("pubDate").text()

        RssItem(title, link, description, pubDate)
    }
    val title = doc.select("title")[0].text()
    val link = doc.select("link")[0].text()
    val desc = doc.select("description")[0].text()

    val rss = Rss(title,link,desc,rssItem)

    println(rss)

}