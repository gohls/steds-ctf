// Complete the isBalanced function below.
    static boolean isBalanced(String s) {
        
        Stack<Character> openBracket = new Stack<Character>();
        // true to start, if s == ""
        // use to break from loop, instead of having multi return statements
        boolean isBalanced = true;
     

        int i = 0;
        while (isBalanced && i < s.length()){
            if (s.charAt(i) == '{' || s.charAt(i) == '(' || s.charAt(i) == '['){
                openBracket.push(s.charAt(i));
            } else if (s.charAt(i) == '}') {
                if (openBracket.isEmpty() || openBracket.pop() != '{'){
                    isBalanced = false;
                }
            } else if (s.charAt(i) == ')') {
                if (openBracket.isEmpty() || openBracket.pop() != '('){
                    isBalanced = false;
                }
            } else if (s.charAt(i) == ']') {
                if (openBracket.isEmpty() || openBracket.pop() != '['){
                    isBalanced = false;
                }
            }
            i++;
        }
        // if open bracket is left, 's' is not balanced
        // ex. ([{}])( 
        if (!openBracket.isEmpty()){
            isBalanced = false;
        }
        return isBalanced;
    }
