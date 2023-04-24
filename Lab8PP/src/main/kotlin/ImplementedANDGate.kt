import java.lang.Exception
import java.util.Vector

class ImplementedANDGate(override val numberOfGates: EntryNumber): ANDGate() {
    override fun operation(values:Vector<Boolean>): Boolean {
        var rez:Boolean
        if(values[0] != true && values[0] != false)
            throw Exception("Not a boolean")
        else rez = values[0]
        for(i in 1 until this.numberOfGates.getEntryNumber()){
            rez = rez and values[i]
        }
        return rez;
    }
}