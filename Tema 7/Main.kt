import java.io.File

fun main(args: Array<String>) {
    var historyList : MutableList<HistoryLogRecord>
    val path: String = "src/main/resources/history.log";

    historyList = readHistory(path);
    historyList.forEach(){
        println("${it.startDate} ${it.comLine}")
    }


}

fun readHistory(path: String): MutableList<HistoryLogRecord>{

    var historyList : MutableList<HistoryLogRecord> = mutableListOf(HistoryLogRecord());
    var startDate : String = "";
    var cmdLine : String = "";


    File(path).forEachLine {
        if(historyList.size <= 50){
            if(it.contains("Start-Date"))
                startDate = it.drop(12);
            if(it.contains("Commandline"))
                cmdLine = it.drop(13);

            if(startDate != "" && cmdLine != ""){
                historyList.add(HistoryLogRecord(startDate,cmdLine))
                startDate = ""
                cmdLine = ""
            }
        }
    }
    return historyList
}

