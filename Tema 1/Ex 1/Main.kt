import java.util.*


fun opgrade(op: Char):Int {
    if(op.toString() == "+" || op.toString() == "-")
        return 1
    if(op.toString() == "*" || op.toString() == "/")
        return 2
    return -1
}

fun isOperator(v : Char) : Boolean {
    val ops = "+-/*"
    var isOpe = false
    for(i in ops.indices)
    {
        if(v == ops[i])
            isOpe = true
    }
    return isOpe
}




fun polishNotation(expr: String):String{
    var polish: Stack<Char> = Stack()
    var res: String = String()
    for(i in expr.indices){
        var c: Char = expr[i]
        if(c.isDigit())
            res += c
        else if(c == '(')
            polish.push(c)
        else if(c == ')'){
            while(polish.isNotEmpty() && polish.peek() != '('){
                res += polish.peek()
                polish.pop()
            }
            polish.pop()
        }
        else {
            while(polish.isNotEmpty() && opgrade(c) <= opgrade(polish.peek())){
                res += polish.peek()
                polish.pop()
            }
            polish.push(c)
        }
    }
    while(polish.isNotEmpty()){
        if(polish.peek() == '(')
            return "invalid"
        res += polish.peek()
        polish.pop()
    }
    return res
}



fun main(args: Array<String>) {
    var readExpression = readln()
    var res = polishNotation(readExpression)
    var a: Float = 0f
    var b: Float = 0f
    var stack =  Stack<Float>()
    var i = 0
    for(i in 0 until res.length){
        if(!isOperator(res[i])){
            stack.push(res[i].digitToInt().toFloat())
            continue
        }
        else {
            var choise = res[i]
            when(choise){
                '+' ->  {
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b+a)

                }
                '-' ->  {
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b-a)
                }
                '*' -> {
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b*a)
                }
                '/' ->  {
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b/a)
                }
                else -> continue

            }
        }
    }
    a = stack.pop()
    print(a)
}
