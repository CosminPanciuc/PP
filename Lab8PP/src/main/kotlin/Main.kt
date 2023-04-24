import java.util.Vector

fun main(args: Array<String>) {
    val andGate2 = ImplementedANDGate(numberOfGates = ANDGate2())
    val andGate3 = ImplementedANDGate(numberOfGates = ANDGate3())
    val andGate4 = ImplementedANDGate(numberOfGates = ANDGate4())
    val andGate8 = ImplementedANDGate(numberOfGates = ANDGate8())
    var values:Vector<Boolean> = Vector<Boolean>()
    values.add(true)
    values.add(false)
    println(andGate2.operation(values))
}