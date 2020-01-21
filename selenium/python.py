# Simple assignment
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

startURL = "https://speedcoding.toptal.com/challenge?ch=toptal-speedcoding"

currentQuestionNu = 1


def getQuestion():
    while True:
        print("looking for Question")
        try:
            return driver.find_element_by_class_name("ace_function").text
        except:
            pass
        time.sleep(0.3)


def getTextarea(prevQuestion):
    while True:
        currentQuestion = getQuestion()
        print("looking for new question, old:", prevQuestion, " new:", currentQuestion)
        try:
            if currentQuestion != prevQuestion:
                textarea = driver.find_element_by_tag_name("textarea")
                return textarea
        except:
            pass
        time.sleep(0.5)


def confirm(textarea):
    wentTillEnd = False
    while True:
        print("Waiting for gree checks")
        try:
            driver.find_element_by_class_name("text-success")
            ActionChains(driver).key_down(Keys.CONTROL, textarea).key_down(
                Keys.RETURN, textarea
            ).perform()
            ActionChains(driver).key_up(Keys.CONTROL).key_up(Keys.RETURN).perform()
            return
        except NoSuchElementException:
            try:
                driver.find_element_by_class_name("alert-danger")
                print("Something is not building - deleting")
                driver.save_screenshot("screenshot.png")
                exit
            except:
                pass

            ActionChains(driver).key_down(Keys.CONTROL, textarea).key_down(
                Keys.RETURN, textarea
            ).perform()
            ActionChains(driver).key_up(Keys.CONTROL, textarea).key_up(
                Keys.RETURN, textarea
            ).perform()


# 43	Pavel Schoffer	425
# 37	Pavel Schoffer	1175
# 34	Pavel Schoffer	2295
# 34	Pavel Schoffer	2311
results = {
    "numberToString": 'return x + ""',
    "double": "return x*2",
    "floatToInt": "return x < 0 ? Math.ceil(x) : Math.floor(x)",
    "square": "return x*x",
    "isEven": "return x % 2 == 0",
    "squareroot": "return Math.sqrt(x)",
    "removeFirstFive": "return x.slice(5)",
    "reverseString": 'return x.split("").reverse().join("")',
    "stringToNumber": "return Number(x.replace(/[^0-9-.]/g,''))",
    "swapHalves": "all = x.split('')\nhalf = all.length / 2\nreturn all.slice(half).join('') + all.slice(0, half).join('')",
    "sumDigits": "cifers = x.toString().split('')\nreturn cifers.reduce((sum, other) => { return ['-', '.'].includes(other) ? sum : sum + Number(other) }, 0)",
    "removeLastFive": "return x.slice(0,-5)",
    "dateRank": 'return Math.round((new Date(x) - new Date("12/31/2018")) / (1000 * 3600 * 24))',
    "oddElements": "var result = []\nfor (var i = 0; i < x.length; i = i + 2) result.push(x[i])\nreturn result",
    "getFileExtension": "var parts = x.split('.')\nreturn parts.length > 1 ? parts[parts.length - 1] : ''",
    "doubleIndex": "return x.filter((item, ix) => { return item == ix * 2 })",
    "longestString": "return x.sort((a, b) => a.length > b.length ? -1 : 1)[0]",
    "hasOnlyVowels": "return x.split('').filter(l => ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'].includes(l)).length === x.length",
    "monthFromUnixTimestamp": "return (new Date(x * 1000)).getMonth() + 1",
    "flatten": "return x.flat(Infinity)",
    "invertCase": "return x.split('').map(l => l.toUpperCase() === l ? l.toLowerCase() : l.toUpperCase()).join('')",
    "sortingType": "function matches(a, b) { var matchItems = a.map((aItem, ix) => aItem == b[ix]); return !matchItems.includes(false) }\nvar sorted = x.concat().sort((a, b) => a < b ? -1 : 1)\nreturn matches(x, sorted) ? 1 : (matches(x.reverse(), sorted) ? -1 : 0)",
    "isBalanced": "var parans = x.split('').filter(c => ['(', ')'].includes(c))\nvar open = 0\nvar broken = false\nparans.forEach(paran => { if (paran === '(') open++; else {broken = broken || open < 1; open--;}});\nreturn !broken && open == 0",
    "mostFrequentNumber": "var dict = {};\nx.forEach(e => e in dict ? dict[e].count++ : dict[e] = { count: 1, value: e });\nhighest = 0\nhighestOccurence = 0\nfor (k in dict) if (dict[k].count > highestOccurence) { highest = dict[k].value; highestOccurence = dict[k].count }\nreturn highest",
    "hasBalancePoint": "if (x.length == 0) return true;\nvar sum = x.reduce((sum, el) => sum += el, 0)\nvar runningSum = 0\nfor (var el of x) { if (runningSum == sum - runningSum) { return true; } else runningSum += el; };\nreturn false",
}


print("Starting")
driver = Chrome()
driver.get(startURL)

print("Went to toptal")

driver.find_element_by_id("leaderboardName").send_keys("Pavel Schoffer")
driver.find_element_by_id("email").send_keys("pavel.schoffer@toptal.com")

driver.find_element_by_tag_name("button").click()

print("Let's do this")

textarea = getTextarea("")
question = getQuestion()

print("Doing: ", question)
while question in results:
    answer = results[question]
    print("Answering: ", answer)
    textarea.send_keys(answer)
    # textarea.send_keys(results["isBalanced"])
    # textarea.send_keys(Keys.ARROW_LEFT)

    confirm(textarea)

    textarea = getTextarea(question)
    question = getQuestion()

print("Unknown!")
driver.save_screenshot("end.png")

