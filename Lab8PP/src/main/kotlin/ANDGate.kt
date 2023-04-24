import java.util.Vector

abstract class ANDGate {
    abstract val numberOfGates: EntryNumber;
    abstract fun operation(values:Vector<Boolean>):Boolean
}