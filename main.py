import streamlit as sl
import pandas as pd

table = pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [8,9,10,11,12,13,14]})

# Remove The Streamlit Hambuger Menu and the streamlit footer
sl.markdown("""
<style>
.css-1rs6os.edgvbvh3
{
    visibility: hidden;
}
.css-cio0dv.egzxvld1
{
    visibility: hidden;
}
</style>    
""", unsafe_allow_html= True)



sl.title("Hi! I am streamlit webapp")

sl.header("Hi! I'm yout header!")

sl.subheader("Hi! I'm your subheader")

sl.text("Hi! I'm a text and programmers uses me as a paragraph tag!")

#  Markdown is a function of streamlit that allow you tu use the markdown markup language
# This is a link for the markdown cheat-sheet: https://www.markdownguide.org/cheat-sheet/
# Example: 
#           **yourText** => is for giving the font the bold style
#            *yourText* => is for giving the font the italic style
#            # yourText => Your markdowk act as a h1 tag
#            ## yourText => Your markdowk act as a h2 tag
#            > yourText => add a blockCode to your text ex:" | Hello world "
#            1. yourText => act as an ordered list <ol> tag
#            - yourText => act as an unordered list <ul> tag
#            ---  => write an horizontal line (good for separing element)
#            [YourText](https://yourLink.com) => act as an anchortag, the title is the text that contain the link 
#            ![alt text](image.jpg) =>  act as an img tag with an alt property set in the [alt text] 
sl.markdown("[Glùglù](https://www.google.com)")
sl.markdown("---")

sl.caption("Hi! i'm a caption!")

# Latex supported functions documentations link: https://katex.org/docs/supported.html
sl.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

# Json functions allows us to add a json code in our application
json={"a":"1,2,3", "b":"4,5,6", "c":"7,8,9"}
sl.json(json)

# .code functions allow us to display coding in our web app
code = """
print("Hello World")
def funct():
    return 0;"""
sl.code(code)

# .write allow us to implement a bunch of different things to our text
sl.write()

# .metric function allow us to display a metrics or different types of metrics
sl.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹")

# .table function allow us to diplay a table on the webapp (the table can be defined with pandas)
sl.table(table)

# .dataframe function allow us to sort our table
sl.dataframe(table)


# .image allow us to use images
sl.image("image.jpg", caption="Hi! this is me!", width=380)

# .audio allow us to use audio
sl.audio("audio.mp3")

# .video allow us to use video
sl.video("video.mp4")



#callback function of the checkbox that print the checkbox state using the checkbox key as identifier
def change():
    print(sl.session_state.checker)

# .checkbox
state = sl.checkbox("Checkbox", value=True, on_change=change, key="checker")

if state:
    sl.write("Hi")
else: 
    pass

# Radio Button (also support the key and the on_change properties)
radio_button = sl.radio("In Which Country Do You Live?", options=("US", "UK", "Canada"))
#print(radio_button)


#Button Function
def btn_click():
    print("Button Clicked")

# Button
btn = sl.button("Click Me", on_click=btn_click)

# .selectbox allow us to select a single option from a drop-down/up menu
select= sl.selectbox("What is your favourite car?", options=("Audi","BMW","Mercedes","Ferrari"))
print(select)

# multiple selectbox allow us to select multiple options from a drop-down/up menu
multi_select = sl.multiselect("What is your favorite Brand?", options=("Microsoft", "Apple", "Amazon", "Oracle"))

sl.write(multi_select)