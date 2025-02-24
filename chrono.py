from datetime import datetime
import pywhatkit as kit

birth={
    "Rani":{"date":"23-02","ph":"+918248917058"},
    "sub":{"date":"23-02","ph":"+919942115521"}
}
today=datetime.now().strftime("%d-%m")

for name,info in birth.items():
    if today==info['date']:kit.sendwhatmsg_instantly(
        info['ph'],
        f"Hi madaam!!!",
        wait_time=30
    )
    print(f"sentt")