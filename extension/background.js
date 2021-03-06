console.log("hello")
alert("sdfsdf")


chrome.runtime.sendMessage({
    action: "getSource",
    source: DOMtoString(document)
});
