import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import altair as alt

df_zomt= pd.read_csv("D:\Dataset\Zomatodataset\zomato.csv",encoding='latin-1')
df_conty=pd.read_excel("D:\Dataset\Zomatodataset\Country-Code.xlsx")
df_final=pd.merge(df_zomt,df_conty,on='Country Code',how="left")

Country_name=df_final.Country.value_counts().index
Country_values=df_final.Country.value_counts().values
plt.pie(Country_values[:4],labels=Country_name[:4],autopct='%1.2f%%')





fig1, ax1 = plt.subplots()
ax1.pie(Country_values[:3],labels=Country_name[:3], autopct='%1.1f%%')
ax1.axis('equal')  
st.subheader("Top 3 countries that uses zomato")
st.pyplot(fig1)
st.write("observation : zomato maximum records or transaction are from india and after that USA  then united kingdom")


st.subheader("Rating")
st.markdown(
                """
                - _when rating is in between 4.5 to 4.9 ---> Excellent_
                - _when rating is in between 4.0 to 4.4 ---> Very Good_
                - _when rating is in between 3.5 to 3.9 ---> Good_
                - _when rating is in between 2.5 to 3.4 ---> Average_
                - _when rating is in between 1.8 to 2.3 ---> Poor_
                - _when rating is 0.0 ---> Not rated_
                """
                )
              
ratings=df_final.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


st.bar_chart(data=ratings,x='Aggregate rating', y='Rating color',use_container_width=True)### observation : 
st.write("observation")
st.markdown(
                """
                - _Not Rated count is very high_
                - _Maximum number of rating are between 2.6 to 4.3_
                """
                ) 

df_final.City.value_counts()
citys_n=df_final.City.value_counts().index
citys_v=df_final.City.value_counts().values


fig2, ax2 = plt.subplots()
ax2.pie(citys_v[:5],labels=citys_n[:5], autopct='%1.1f%%')
ax2.axis('equal')  
st.subheader("top 5 cities distribution zomato")
st.pyplot(fig2)
st.write("observation : zomato maximum records or transaction are from india and after that USA  then united kingdom")


fig3, ax3 = plt.subplots()
ax3.pie(citys_v[:5],labels=citys_n[:5], autopct='%1.1f%%')
ax3.axis('equal')  
st.subheader("top 5 cities distribution zomato")
st.pyplot(fig3)
st.write("observation : zomato maximum records or transaction are from india and after that USA  then united kingdom")


Cuisines_c=df_final['Cuisines'].value_counts().reset_index()
top_10_cuisines=Cuisines_c.sort_values(by='count', ascending=False).head(10)

# st.bar_chart(top_10_cuisines)

bar_chart = alt.Chart(top_10_cuisines).mark_bar().encode(
    x="count",
     y=alt.Y("Cuisines", sort="-x")
)

st.altair_chart(bar_chart, use_container_width=True)
