class HistoryLogRecord() : Comparable<HistoryLogRecord>{
    var startDate : String = "";
    var comLine : String = "";

    constructor(startDate : String, comLine : String) : this() {
        this.startDate = startDate;
        this.comLine = comLine;
    }


    override fun compareTo(other: HistoryLogRecord): Int {
        if(this.startDate < other.startDate)
            return -1;
        if(this.startDate > other.startDate)
            return 1;
        return 0;
    }
}