import plotly.express as px
import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
from millify import millify

st.set_page_config(layout="wide")

# Styling of metric container
st.markdown("""
  <style>
  div[data-testid="metric-container"] {
     background-color: #424b43;
     border: 3px solid #111212;
     padding: 5% 5% 5% 10%;
     border-radius: 10px;
     color: white;
     overflow-wrap: break-word;
  }

  /* breakline for metric text         */
  div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
     overflow-wrap: break-word;
     white-space: break-spaces;
     color: #B7e493;
  }
  </style>
  """, unsafe_allow_html=True)

# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide"
#     # initial_sidebar_state="expanded"
#     # }
# )

# -------------------------------------------------------------------------------------------------------------------------------------

with st.sidebar:
  st.header("Navigation:")
  st.markdown("""
  - [Introduction](https://arbitrum-governance.streamlit.app/~/+/#introduction)
    - [Arbitrum](https://arbitrum-governance.streamlit.app/~/+/#arbitrum)
    - [Arbitrum Governance](https://arbitrum-governance.streamlit.app/~/+/#arbitrum-governance)
    - [Importance of Governance](https://arbitrum-governance.streamlit.app/~/+/#importance-of-governance)
    - [Community Participation](https://arbitrum-governance.streamlit.app/~/+/#community-participation)
    - [Differences Between Tally, Karma and Snapshot](https://arbitrum-governance.streamlit.app/~/+/#Differences-Between-Tally,-Karma-and-Snapshot)
  - [Overview](https://arbitrum-governance.streamlit.app/~/+/#overview)
    - [Elliptic's Methdology](#elliptic-s-methdology)
    - [BitOK's Methodology](#bitok-s-methdology)
  - [THE REALITY](#the-reality)
    - [Crypto Aid Israel](#crypto-aid-israel)
    - [UkraineDAO](#ukrainedao)
    - [Top High Impact Crypto Based Humanitarian Projects](#top-high-impact-crypto-based-humanitarian-projects)
  - [CONCLUSION](#conclusion)
  """)

st.markdown(f'<h1 style="background-image:url(https://imageio.forbes.com/specials-images/imageserve/5f6e5a2d793c5299630c7bf3/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds);font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"Arbitrum Governance Participation Analysis."}</h1>', unsafe_allow_html=True)

# -------------------------------------------------------------------------------------------------------------------------------------


# csv1 = pd.read_csv("csv_data/Overall_Proposal_Id_Stats.csv", on_bad_lines='skip')



# st.image("https://static.timesofisrael.com/www/uploads/2023/07/hamas.jpg", width=1000, use_column_width=False)


#   sellected = sac.menu([
#       sac.MenuItem('home', icon='house-fill'),
#       sac.MenuItem('products', icon='box-fill', children=[
#           sac.MenuItem('apple', icon='apple', tag=sac.Tag('USA', color='green', bordered=False)),
#           sac.MenuItem('other', icon='git', children=[
#               sac.MenuItem('google', icon='google'),
#               sac.MenuItem('gitlab', icon='gitlab'),
#               sac.MenuItem('wechat' * 5, icon='wechat'),
#           ]),
#       ]),
#       sac.MenuItem('disabled', icon='send', disabled=True),
#       sac.MenuItem(type='divider'),
#       sac.MenuItem('reference', type='group', children=[
#           sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
#           sac.MenuItem('bootstrap-icon', icon='bootstrap', href='https://icons.getbootstrap.com/'),
#       ]),
#   ], format_func='title', open_all=True)

# if sellected == "home":
# else:
# st.write("settings is my bettings")



# -------------------------------------------------------------------------------------------------------------------------------------

# url1 = pd.read_json("https://flipsidecrypto.xyz/api/v1/queries/db6b10f5-8031-4143-893d-6d6346be873f/data/latest")
# st.dataframe(url1)

# --------------------------------------------------------------------------------------------------------------------------------------


# cola, colb, colc = st.columns([1,3,1])

# with colb:
#   st.markdown("""
#   ### :blue[Overall Proposal Id On-chain Stats on Arbitrum]
#   """)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


st.header("INTRODUCTION")

st.markdown("""
## **Arbitrum** 

This is a **Layer 2 scaling solution** for Ethereum. It aims to enhance scalability, reduce transaction costs, and improve user experience. **Optimistic Rollup** is the underlying technology used by Arbitrum.

 ### **Arbitrum Governance**:
 
  - **Decentralized Autonomous Organizations (DAOs)** play a crucial role in governing the Arbitrum network.
  - Participants in the ecosystem have the opportunity to influence decisions and protocols.
  - Key aspects of Arbitrum governance include:
      - **Proposal Submission**: Anyone can propose changes or improvements.
      - **Voting**: Token holders vote on proposals.
      - **Implementation**: Approved proposals are implemented by developers.

### **Importance of Governance**:
  - Effective governance ensures the network's evolution aligns with community values.
  - It impacts parameters like **gas fees**, **security**, and **protocol upgrades**.

### **Community Participation**:
  - **Tally**, **Karma**, and **Snapshot** are platforms used for governance participation.
  - Each platform has unique features, such as on-chain/off-chain voting and gasless options.
  - Choose the platform that best suits your preferences and project goals.

Remember, **Arbitrum governance** empowers the community to shape the network's future.

Let's quickly explore the differences between **Tally**, **Karma**, and **Snapshot** as governance participation platforms for the **Arbitrum network**:

1. **Tally**:
    - **Type**: **On-chain** governance platform.
    - **Functionality**:
        - Provides a **plug-and-play UI and API** for standard DAO governance contracts.
        - Users can **directly vote on proposals on the blockchain**.
        - Requires users to pay **gas fees** for voting.
        - Recorded votes are **on-chain** and transparent.
    - **Use Case**:
        - Ideal for projects that prioritize **fully decentralized and transparent voting**.
        - Suitable for users who are comfortable with paying gas fees.
    - **Source**: ¹².

2. **Karma**:
    - **Type**: **Off-chain** governance tool.
    - **Functionality**:
        - Developed by the team behind the **Balancer exchange**.
        - Enables **gasless voting** through off-chain messages.
        - Used for **signal polls** and community sentiment gauging.
        - Votes are **not submitted and broadcast on-chain**.
        - Requires a **trusted entity** to review and execute results.
    - **Use Case**:
        - Useful for projects aiming to **minimize transaction fees** for users.
        - Often adopted alongside an **on-chain voting system** for proposal ratification.
    - **Source**: ¹.

3. **Snapshot**:
    - **Type**: **Off-chain** governance tool.
    - **Functionality**:
        - Enables **gasless voting** by taking **snapshots** of token balances.
        - Users sign messages off-chain to cast votes.
        - Votes are stored via **decentralized file storage** (e.g., IPFS or Arweave).
        - **Not directly submitted on-chain**; requires a trusted entity for final vote count.
        - Used by various projects, including **Yearn Finance** and **Sushiswap**.
    - **Use Case**:
        - Suitable for projects seeking a balance between **cost-effective voting** and **transparency**.
    - **Source**: ¹.

In summary, **Tally** provides on-chain voting, **Karma** focuses on gasless off-chain voting, and **Snapshot** combines off-chain voting with decentralized storage. Choose the platform that aligns best with your project's goals and user preferences. 🗳️✨
""")

st.markdown("""
## Overview

This dashboard provides an analysis of on-chain governance participation rate, which is a measure of how active and engaged the token holders are in the decision-making process of a decentralized organization (DAO). The dashboard aims to achieve the following goals:

- Increase participation rates in on-chain voting of Arbitrum DAO.
- Enhance DAO legitimacy

The dashboard covers the following aspects of on-chain governance participation:

- Holder metrics: The number and distribution of token holders and their voting power
- Proposal metrics: The number and outcome of governance proposals and their categories
- Participation metrics: The voting turnout and behavior of token holders and delegates
- Impact metrics: The effect of on-chain governance participation on the DAO's performance and reputation

The dashboard uses data from [flipsidecrypto](flipsidecrypto.xyz) as the major source and compared to [Karma](karma.xyz) and [Tally](tally.xyz) for on-chain data, and [Snapshot](snapshot.org) for off-chain data, to provide a comprehensive and comparative view of on-chain governance participation across different DAOs.
""")

# ------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
## :red[1. ON-CHAIN PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE(Compared To Karma and Tally)]
""")


# ------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------

csva = pd.read_csv("csv_data/Total_Proposals.csv")
csvb = pd.read_csv("csv_data/Percent_Arb_Delegated.csv")
csvc = pd.read_csv("csv_data/Total_Voters.csv")

col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
with col_1:
  st.metric(label="Proposals", value=(millify(csva["PROPOSALS"][0], precision=2)))
with col_2:
  st.metric(label="Proposers", value=(millify(csva["PROPOSERS"][0], precision=2)))
with col_3:
  st.metric(label="Delegators", value=(millify(csvb["DELEGATOR"][0], precision=2)))
with col_4:
  st.metric(label="Voters", value=(millify(csvc["VOTERS"][0], precision=2)))

with col_1:
  st.metric(label="Total ARB", value=(millify(csvb["TOTAL_SUPPLY"][0], precision=2)))
with col_2:
  st.metric(label="Circulating Supply", value=(millify(csvb["CIRCULATING_SUPPLY"][0], precision=2)))
with col_3:
  st.metric(label="ARB Delegated", value=(millify(csvb["AMOUNT_DELEGATED"][0], precision=2)))
with col_4:
  st.metric(label="% Circulating ARB", value=(millify(csvb["PERCENT_DELEGATED"][0], precision=2)))

with col_1:
  st.metric(label="Votes", value=(millify(csvc["VOTES"][0], precision=2)))
with col_2:
  st.metric(label="Voted For", value=(millify(csvc["FOR"][0], precision=2)))
with col_3:
  st.metric(label="Voted Against", value=(millify(csvc["AGAINST"][0], precision=2)))
with col_4:
  st.metric(label="Abstain", value=(millify(csvc["ABSTAIN"][0], precision=2)))

st.markdown("""
### COMMENTS
Onchain, a total of 29 proposals proposed by 9 unique proposers has been voted upon on the Arbitrum governance.

Of the 2.65billion ARBS in circulation, only 321.5million ARBs are available for voting in governance (delegated). This makes just about 12% of the currently circulating ARBs. This is quite a small amount.

A total of approximately 620k votes has been made by 136k voters out of which a significant portion (524k) voted in favor of the proposals while a smaller number voted against and some abstained from picking a choice.
""")


# --------------------------------------------------------------------------------------------------------------------------------------

csv4 = pd.read_csv("csv_data/arb_token_supply.csv", sep=';')

# Create the new column by dividing 'marketCap' by 'close'
csv4['circulating_supply'] = csv4['marketCap'] / csv4['close']
csv4['token_supply'] = 10000000000

# st.dataframe(csv4)

# st.metric(label="Circulating Supply", value=(millify(csv4["circulating_supply"][360], precision=2)))

fig_1 = px.bar(csv4, x="timestamp", y="marketCap", title="Daily Marketcap of Arb Token", height=500,) 
# log_y=True)
fig_1.update_layout(hovermode="x unified")
# Add Scatter plot
fig_1.add_scatter(x=csv4['timestamp'], y=csv4['volume'], name="Volume", line_color="red")
# fig_1.add_scatter(x=csv4['timestamp'], y=csv4['circulating_supply'], name="Circulating Supply", line_color="red")
st.plotly_chart(fig_1, use_container_width=True)


# ----------------------------------------------------------------------------------------------------

csvd = pd.read_csv("csv_data/Percent_Arb_Delegated_copy.csv")
csv5 = pd.read_csv("csv_data/Onchain_Holders(Voters)_Stats_of_Arbitrum.csv")
csve = pd.read_csv("csv_data/Ghost_Delegate_vs_Voting_Delegates.csv")

col_1, col_2 = st.columns(2, gap='large')
with col_1:
  subfig = make_subplots(specs=[[{"secondary_y": True}]])

  # create two independent figures with px.line each containing data from multiple columns
  fig = px.line(csvd, x="TIMESPAN", y=["DELEGATORS", "DELEGATES"])
  fig2 = px.line(x=csvd['TIMESPAN'], y=csvd['DEL_BALANCES'])
  # name="CUMUL_NETFLOW", line_color="yellow")

  fig2.update_traces(yaxis="y2")

  subfig.add_traces(fig.data + fig2.data)
  subfig.layout.xaxis.title="Timespan"
  subfig.layout.yaxis.title="User Count"
  # subfig.layout.yaxis2.type="log"
  subfig.layout.yaxis2.title="Amount Delegated"
  subfig.update_layout(hovermode="x unified", title="Weekly Delegates vs Delegators vs Delegated ARB", height=500)
  # recoloring is necessary otherwise lines from fig und fig2 would share each color
  # e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
  subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
  st.plotly_chart(subfig, use_container_width=True)

with col_2:
  fig_2a = px.bar(csv5, x="TYPE", y="HOLDERS", title="Holders Distribution Stats", height=500, color="TYPE") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)


st.markdown("""
### COMMENTS
- TOTAL HOLDERS: this is the number of holders that was gotten from the ARB token contract [page](https://arbiscan.io/token/0x912ce59144191c1204e64559fe8253a0e49e6548).
- NON-VOTERS: This is a subtraction of the total voters and the number of wallets that has ever voted onchain.
-NON-VOTING HOLDERS: These are holders based onchain balance that have not participated in onchain governance. These are the largest set of the grouping next to the total holder and non-voters. This is actually not a good number.
- HOLDERS(bal>0): are defined as users with more than zero balance in their wallets. It is important to note that these are not the exact values of individual holders but an estimated number from onchain data, delegator and delegate ARBs are locked 🔒 in a contract and does not reflect as balance in their wallets. But these are still the largest of all the holders distribution stats.
- DELEGATES: These are wallets that tokens has been delegated to for voting.
- GHOST DELEGATES: These are delegates that has received delegations but has never participated in any onchain voting. This makes a very high percentage(62%) of the delegates on the ARB governance.
-VOTERS: These are wallets that has participated in voting activities on the Arbitrum governance.
- NON-DELEGATE VOTERS: This constitutes a small portion of voters that are not delegates but are participating in Arbitrum governance.
""")
  # -----------------------------------------------------------------------------------------------------------------------

with col_1:
  fig_2a = px.bar(csve, x="TYPE", y="HOLDERS", title="Ghost Delegate vs Voting Delegates", height=500, color="TYPE") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_2:
  fig_2b = px.pie(csve, names="TYPE", values="HOLDERS",
             color='TYPE', title="PERCENT Delegate vs Voting Delegates",
             height=500)
  fig_2b.update_layout(hovermode="x unified")
  fig_2b.update_traces(textposition='inside', textinfo='percent+label')
  st.plotly_chart(fig_2b, use_container_width=True)

# with col_2:
#   fig_2b = px.bar(csv5, x="TYPE", y="PERCENT", title="PERCENT Holders Distribution Stats", height=500, color="TYPE") 
# # log_y=True)
#   fig_2b.update_layout(hovermode="x unified")
#   st.plotly_chart(fig_2b, use_container_width=True)


# --------------------------------------------------------------------------------------------------------------------------------------

csv6 = pd.read_csv("csv_data/Delegates_Distribution_by_Wallet_Size.csv")

# st.dataframe(csv6)

size_max_default = 20
scaling_factor = 4

fig_3 = px.scatter(
    csv6,
    x='ENS',
    y='WALLET_SIZE',
    color='WALLET_SIZE',
    size='ARB_DELEGATED',
    size_max=size_max_default*scaling_factor,
    title='Delegates Distribution by Wallet Size(Arb Delegated)',
    height= 500
)
# fig_3.update_traces(marker={'size': 30})

st.plotly_chart(fig_3, use_container_width=True)


fig_3a = px.scatter(
    csv6,
    x='ENS',
    y='WALLET_SIZE',
    color='WALLET_SIZE',
    size='USER_DELEGATED',
    size_max=size_max_default*scaling_factor,
    title='Delegates Distribution by Wallet Size(User Delegated)',
    height= 500
)

st.plotly_chart(fig_3a, use_container_width=True)

st.markdown("""
### COMMENTS

SQL credits for this chart goes to [PANDA](), a flipsidecrypto fata analyst on his work on [Arbitrum Governance]().

This distribution was strategically placed based on the amount of ARBs delegated and the number of delegators, the findings are quite insightful.

Based on the ARBs delegated, a lot of delegates (top 50 to be precise) received a very high amount of delegations greater than 1000ARBs and this constitutes a majority of the ARB delegated to them.

What offsets the above finding os that, based on users delegating, most wallets delegated less than 100ARBs to the delegates.

This means that, majority of the voting power of most of these delegates came from a few selected whales. This looks like a centralization issue.
""")



# --------------------------------------------------------------------------------------------------------------------------------------


csvf = pd.read_csv("csv_data/Weekly_Voters_Stats.csv")
col_1, col_2, col_3 = st.columns(3, gap='large')

with col_1:
  fig_2a = px.line(csvf, x="TIMESPAN", y="VOTERS", title="For, Against & Abstain by Voters Count", height=500, color="VOTE_OPTION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_2:
  fig_2a = px.line(csvf, x="TIMESPAN", y="CUMUL_VOTERS", title="Cumulative For, Against & Abstain by Voters Count", height=500, color="VOTE_OPTION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_3:
  fig_2a = px.histogram(csvf, x="VOTE_OPTION", y="VOTERS", title="Vote Options by Voters Count", height=500, color="VOTE_OPTION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

# ----------------------------------------------------------------------

with col_1:
  fig_2a = px.line(csvf, x="TIMESPAN", y="VOTES", title="For, Against & Abstain by Vote Count", height=500, color="VOTE_OPTION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_2:
  fig_2a = px.line(csvf, x="TIMESPAN", y="CUMUL_VOTES", title="Cumulative For, Against & Abstain by Vote Count", height=500, color="VOTE_OPTION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_3:
  fig_2a = px.histogram(csvf, x="VOTE_OPTION", y="VOTES", title="Vote Options by Vote Count", height=500, color="VOTE_OPTION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

# --------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
### :blue[Who publishes proposals most often.]
""")

csvg = pd.read_csv("csv_data/Who_publishes_proposals_most_often..csv")

col_1, col_2 = st.columns(2, gap='large')
with col_1:
  st.dataframe(csvg)

with col_2:
  fig_2b = px.pie(csvg, names="PROPOSER_SHORT", values="PROPOSALS",
             color='PROPOSER_SHORT', title="Who Publishes Proposals Most Often",
             height=500)
  fig_2b.update_layout(hovermode="x unified")
  fig_2b.update_traces(textposition='inside', textinfo='percent+label')
  st.plotly_chart(fig_2b, use_container_width=True)

st.markdown("""
### COMMENTS

ENS name  0xfrisson with wallet address 0xb5b069370ef24bc67f114e185d185063ce3479f8 is seen to be the one with the highest number of proposals on the Arbitrum governance with a total of 13 proposals out of 29. That is more than 44% of all the proposals on the governance.
""")
# --------------------------------------------------------------------------------------------------------------------------

st.markdown("""
### :blue[Which categories of users take part more often.]
""")

csvh = pd.read_csv("csv_data/Which_categories_of_users_take_part_more_often.csv")
csvi = pd.read_csv("csv_data/Voters_Participation_by_Votes.csv")
csvj = pd.read_csv("csv_data/Voters_Participation_by_days.csv")

col_1, col_2 = st.columns(2, gap='large')
with col_1:
  fig_2a = px.bar(csvh, x="USER_TYPE", y="VOTERS", title="Which categories of users take part more often(Voters Count)", height=500, color="USER_TYPE") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

  fig_2a = px.bar(csvi, x="PARTICIPATION", y="VOTERS", title="Voters Participation by Votes", height=500, color="PARTICIPATION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_2:
  fig_2a = px.bar(csvh, x="USER_TYPE", y="TXES", title="Which categories of users take part more often(Tx Count)", height=500, color="USER_TYPE") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

  fig_2a = px.bar(csvj, x="PARTICIPATION", y="VOTERS", title="Voters Participation by Days", height=500, color="PARTICIPATION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

st.markdown("""
### COMMENTS
While trying to find out which categories of users take part more often in voting on the Arbitrum governance we decided to see the number of votes, days and the other contracts that voters have been interacting with. Some interesting discoveries were made.

- A very large number of voters has participated in voting about 2-5 times indicating that there are indeed repeat voters involved in the governance.
- More users voted within one day showing little commitment by most voters to the Arbitrum governance. Although a lot of return voters between 2-5days were also recorded.
- By voters count interacting with contracts, bridging and dex users are the prominent voters on the Arbitrum governance.
- Checking for transaction count, it was very clear that most voters were bridgers.
- Questions that arose were: are those users bridging in or out of the Arbitrum chain, what tokens do they interact with the most and do they participate in governance on other chains. 
""")


# ------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
## :red[2. SNAPSHOT PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE]
""")


# ------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------

csva = pd.read_csv("csv_data/Snapshop_Proposal_Id_Overview.csv")
csvb = pd.read_csv("csv_data/Percent_Arb_Delegated.csv")
csvc = pd.read_csv("csv_data/Total_Voters.csv")

col_1, col_2, col_3 = st.columns(3, gap='large')
with col_1:
  st.metric(label="Proposals", value=(millify(csva["PROPOSAL"][0], precision=2)))
with col_2:
  st.metric(label="Proposers", value=(millify(csva["PROPOSERS"][0], precision=2)))
with col_3:
  st.metric(label="Voters", value=(millify(csva["VOTERS"][0], precision=2)))

col_1, col_2, col_3, col_4 = st.columns(4, gap='large')
with col_1:
  st.metric(label="Votes", value=(millify(csva["VOTES"][0], precision=2)))
with col_2:
  st.metric(label="Voted For", value=(millify(csva["FOR"][0], precision=2)))
with col_3:
  st.metric(label="Voted Against", value=(millify(csva["AGAINST"][0], precision=2)))
with col_4:
  st.metric(label="Abstain", value=(millify(csva["ABSTAIN"][0], precision=2)))

# ----------------------------------------------------------------------------------------------------

csvk = pd.read_csv("csv_data/Daily_Snapshot_Proposal_Id_Overview.csv")


col_1, col_2, col_3 = st.columns(3, gap='large')
with col_1:
  fig_2a = px.bar(csvk, x="TIMESPAN", y="PROPOSAL", title="Daily Proposals vs Proposers", height=500) 
# log_y=True)
  fig_2a.add_scatter(x=csvk['TIMESPAN'], y=csvk['PROPOSERS'], name="Poposers", line_color="red")
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_2:
  fig_2a = px.line(csvk, x="TIMESPAN", y=["FOR", "AGAINST", "ABSTAIN"], title="Daily Vote Options", height=500) 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_3:
  fig_2a = px.line(csvk, x="TIMESPAN", y=["CUMUL_FOR", "CUMUL_AGAINST", "CUMUL_ABSTAIN"], title="Cumulative Vote Options", height=500) 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

  # -----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
### :blue[Who publishes proposals most often.]
""")

csvg = pd.read_csv("csv_data/Who_publishes_proposals_most_often_(Snapshot).csv")

col_1, col_2 = st.columns(2, gap='large')
with col_1:
  st.dataframe(csvg)

with col_2:
  fig_2b = px.pie(csvg, names="NAME", values="PROPOSALS",
             color='NAME', title="Who Publishes Proposals Most Often)",
             height=500)
  fig_2b.update_layout(hovermode="x unified")
  fig_2b.update_traces(textposition='inside', textinfo='percent+label')
  st.plotly_chart(fig_2b, use_container_width=True)

# --------------------------------------------------------------------------------------------------------------------------

st.markdown("""
### :blue[Which categories of users take part more often.]
""")

csvh = pd.read_csv("csv_data/Which_categories_of_users_take_part_more_often.csv")
csvi = pd.read_csv("csv_data/Voters_Participation_by_Votes.csv")
csvj = pd.read_csv("csv_data/Voters_Participation_by_days.csv")

col_1, col_2 = st.columns(2, gap='large')
with col_1:
  fig_2a = px.bar(csvh, x="USER_TYPE", y="VOTERS", title="Which categories of users take part more often(Voters Count)", height=500, color="USER_TYPE") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

  fig_2a = px.bar(csvi, x="PARTICIPATION", y="VOTERS", title="Voters Participation by Votes", height=500, color="PARTICIPATION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_2:
  fig_2a = px.bar(csvh, x="USER_TYPE", y="TXES", title="Which categories of users take part more often(Tx Count)", height=500, color="USER_TYPE") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

  fig_2a = px.bar(csvj, x="PARTICIPATION", y="VOTERS", title="Voters Participation by Days", height=500, color="PARTICIPATION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
## :red[1. ON-CHAIN STATS OF ARBITRUM GOVERNANCE(Compared To Karma and Tally)]
""")


# --------------------------------------------------------------------------------

st.markdown("""
### :blue[Overall Proposal Id On-chain Stats on Arbitrum]
""")

csv1 = pd.read_csv("csv_data/Overall_Proposal_Id_Stats.csv", on_bad_lines='skip')

st.dataframe(csv1)

fig_1 = px.bar(csv1, x="DATE_CREATED", y=["FOR", "AGAINST", "ABSTAIN"], title="Daily Marketcap of Arb Token", barmode='group', height=500) 
# log_y=True)
fig_1.update_layout(hovermode="x unified")
# Add Scatter plot
fig_1.add_scatter(x=csv1['DATE_CREATED'], y=csv1['TOTAL_VOTES'], name="Total Votes", line_color="red")
# fig_1.add_scatter(x=csv4['timestamp'], y=csv4['circulating_supply'], name="Circulating Supply", line_color="red")
st.plotly_chart(fig_1, use_container_width=True)



with st.expander("See Overall Proposal Id Stats SQL"):
  st.header("Check out query on Flipside [link](https://flipsidecrypto.xyz/zackmendel/q/fRLsaIH24jpz/overall-proposal-id-stats-on-chain-against-tally)")
  code = '''
WITH delegates AS (
SELECT
  DISTINCT decoded_log:delegate AS delegate
FROM arbitrum.core.fact_decoded_event_logs
  WHERE contract_address = '0x912ce59144191c1204e64559fe8253a0e49e6548'
  AND event_name = 'DelegateVotesChanged'
),

delegate_power AS (
SELECT
  DISTINCT decoded_log:voter AS voter,
  max(decoded_log:weight/pow(10,18)) AS delegate_power,
  max (block_timestamp::date) AS max_date
FROM arbitrum.core.fact_decoded_event_logs
  WHERE contract_address IN ('0x789fc99093b09ad01c34dc7251d0c89ce743e5a4', '0xf07ded9dc292157749b6fd268e37df6ea38395b9')
  AND event_name = 'VoteCast'
  AND decoded_log:voter IN (SELECT delegate FROM delegates)
GROUP BY 1
),

proposer AS (
SELECT
  DISTINCT decoded_log:proposalId AS proposalId,
  decoded_log:proposer AS proposer,
  decoded_log:description AS description
FROM arbitrum.core.fact_decoded_event_logs
  WHERE contract_address IN ('0x789fc99093b09ad01c34dc7251d0c89ce743e5a4', '0xf07ded9dc292157749b6fd268e37df6ea38395b9')
  AND event_name = 'ProposalCreated'
)

SELECT
  decoded_log:proposalId AS proposal_id,
  proposer,

  CASE
    WHEN contract_address = '0x789fc99093b09ad01c34dc7251d0c89ce743e5a4' THEN 'Arbitrum Treasury'
    WHEN contract_address = '0xf07ded9dc292157749b6fd268e37df6ea38395b9' THEN 'Arbitrum Core'
  END as governor,

  CASE
    WHEN contract_address = '0x789fc99093b09ad01c34dc7251d0c89ce743e5a4' THEN '76730000'
    WHEN contract_address = '0xf07ded9dc292157749b6fd268e37df6ea38395b9' THEN '127880000'
  END as quorum_needed,

  -- decoded_log:support AS support,

  sum (CASE WHEN decoded_log:support = '1' THEN 1 END) AS "FOR",
  sum (CASE WHEN decoded_log:support = '0' THEN 1 END) AS against,
  sum (CASE WHEN decoded_log:support = '2' THEN 1 END) AS abstain,

  -- CASE
  --   WHEN decoded_log:support = '1' THEN 'For'
  --   WHEN decoded_log:support = '0' THEN 'Against'
  --   ELSE 'Abstain'
  -- END AS vote_option,

  -- decoded_log:voter AS voter,
  COUNT (DISTINCT tx_hash) AS total_votes,
  sum (decoded_log:weight/pow(10,18)) AS weight,
  weight/ quorum_needed * 100 AS percent_quorum,
  CASE
    WHEN percent_quorum > 100 THEN 'Passed'
    ELSE 'Failed'
  END AS status,
  description
  -- decoded_log:reason AS reason
FROM arbitrum.core.fact_decoded_event_logs e JOIN proposer p 
ON e.decoded_log:proposalId = p.proposalId
  WHERE contract_address IN ('0x789fc99093b09ad01c34dc7251d0c89ce743e5a4', '0xf07ded9dc292157749b6fd268e37df6ea38395b9')
  AND event_name = 'VoteCast'
GROUP BY proposal_id, governor, quorum_needed, proposer, description--, support
ORDER BY proposal_id
LIMIT 100
'''
  st.code(code, language="sql")

# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------

st.markdown("""
### :blue[Overall Voters On-chain Stats on Arbitrum]
""")

csv2 = pd.read_csv("csv_data/Overall_Voters_Stats.csv", on_bad_lines='skip')

st.dataframe(csv2)



with st.expander("See Overall Voters Stats SQL"):
  st.header("Check out query on Flipside [link](https://flipsidecrypto.xyz/edit/queries/4cc87be6-995f-4b4d-b945-38e10aa6f316)")
  code = '''
WITH delegates AS (
SELECT
  DISTINCT decoded_log:delegate AS delegate
FROM arbitrum.core.fact_decoded_event_logs
  WHERE contract_address = '0x912ce59144191c1204e64559fe8253a0e49e6548'
  AND event_name = 'DelegateVotesChanged'
),

delegate_power AS (
SELECT
  DISTINCT decoded_log:voter AS delegate,
  max(decoded_log:weight/pow(10,18)) AS delegate_power,
  max (block_timestamp::date) AS max_date
FROM arbitrum.core.fact_decoded_event_logs 
  WHERE contract_address IN ('0x789fc99093b09ad01c34dc7251d0c89ce743e5a4', '0xf07ded9dc292157749b6fd268e37df6ea38395b9')
  AND event_name = 'VoteCast'
  AND decoded_log:voter IN (SELECT delegate FROM delegates)
GROUP BY 1
),

max_date AS (
SELECT
  DISTINCT owner AS owners,
  max (last_registered_timestamp) AS max_date
FROM crosschain.ens.ez_ens_domains
  WHERE expired != 'FALSE'
GROUP BY 1
),

enss AS (
SELECT
  DISTINCT owner,
  ens_domain AS ens
FROM crosschain.ens.ez_ens_domains e JOIN max_date m
ON e.owner = m.owners AND e.last_registered_timestamp = m.max_date
  WHERE expired != 'FALSE'
ORDER BY 1 
),

stats AS (
SELECT
  decoded_log:voter AS voter,
  CASE
    WHEN contract_address = '0x789fc99093b09ad01c34dc7251d0c89ce743e5a4' THEN 'Arbitrum Treasury'
    WHEN contract_address = '0xf07ded9dc292157749b6fd268e37df6ea38395b9' THEN 'Arbitrum Core'
  END as governor,

  CASE
    WHEN contract_address = '0x789fc99093b09ad01c34dc7251d0c89ce743e5a4' THEN '76730000'
    WHEN contract_address = '0xf07ded9dc292157749b6fd268e37df6ea38395b9' THEN '127880000'
  END as quorum_needed,

  sum (CASE WHEN decoded_log:support = '1' THEN 1 END) AS "FOR",
  sum (CASE WHEN decoded_log:support = '0' THEN 1 END) AS against,
  sum (CASE WHEN decoded_log:support = '2' THEN 1 END) AS abstain,

  -- decoded_log:reason AS reason,
  COUNT (DISTINCT tx_hash) AS votes
FROM arbitrum.core.fact_decoded_event_logs 
  WHERE contract_address IN ('0x789fc99093b09ad01c34dc7251d0c89ce743e5a4', '0xf07ded9dc292157749b6fd268e37df6ea38395b9')
  AND event_name = 'VoteCast'
GROUP BY voter, governor, quorum_needed
)

SELECT
  -- ens.ens_domain AS ens,
  delegate,
  governor,
  "FOR",
  against,
  abstain,
  votes,
  delegate_power,
  delegate_power/quorum_needed *100 AS percent_quorum
FROM stats s JOIN delegate_power d 
ON s.voter = d.delegate
-- JOIN crosschain.ens.ez_ens_domains ens
-- ON delegate = ens.owner
ORDER BY delegate_power DESC
LIMIT 1000
'''
  st.code(code, language="sql")

# --------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
### :blue[Overall Proposal Id Stats for the first 1000 Proposals by Vote Count of Arbitrum on Snapshot.]
""")

csv3 = pd.read_csv("csv_data/Overall_Voters_Stats.csv", on_bad_lines='skip')

st.dataframe(csv3)



with st.expander("See Snapshot Proposal Id Stats SQL"):
  st.header("Check out query on Flipside [link](https://flipsidecrypto.xyz/zackmendel/q/AuVY4DTI_hSB/snapshot-base-query)")
  code = '''
WITH delegates AS (
WITH dates AS (
SELECT
  DISTINCT proposal_id AS id,
  created_at::date AS date_created
FROM external.snapshot.fact_proposals
  WHERE network = 'arbitrum'
)


SELECT
  DISTINCT proposal_id,
  date_created,
  proposal_title AS title,
  proposal_author AS proposer,
  sum (CASE WHEN vote_option[0] = '1' THEN 1 END) AS "FOR",
  sum (CASE WHEN vote_option[0] = '2' THEN 1 END) AS against,
  sum (CASE WHEN vote_option[0] != '2' AND vote_option[0] != '1' THEN 1 END) AS abstain,
  COUNT (DISTINCT voter) AS votes,
  sum (voting_power) AS voting_power,
  quorum,
  proposal_text
FROM external.snapshot.ez_snapshot s JOIN dates d
ON s.proposal_id = d.id
  WHERE network = 'arbitrum'
  AND quorum IS NOT NULL
GROUP BY 1, 2, 3, 4, quorum, proposal_text
ORDER BY votes DESC
LIMIT 1000
'''
  st.code(code, language="sql")

# --------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
## REFERENCES

(1) For decentralized governance on Ethereum, why is Snapshot considered .... https://ethereum.stackexchange.com/questions/127331/for-decentralized-governance-on-ethereum-why-is-snapshot-considered-off-chain.
(2) Snapshot Polls | Tally Docs. https://docs.tally.xyz/education/governance-frameworks/snapshot-polls.
(3) What's the difference between Tally vs Snapshot? : r/dao - Reddit. https://www.reddit.com/r/dao/comments/sbjbpn/whats_the_difference_between_tally_vs_snapshot/.
(4) Tally - Run DAOs onchain. https://www.tally.xyz/.
(5) undefined. https://ethereum.stackexchange.com/a/127351.
(6) Use Snipping Tool to capture screenshots - Microsoft Support. https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b.
(7) Lightshot — screenshot tool for Mac & Win. https://app.prntscr.com/.
(8) Snipaste - 截图 + 贴图. https://zh.snipaste.com/.
(9) Download Now - TallyPrime 4.1, TallyPrime Server & Developer. https://tallysolutions.com/download/.
(10) TallyPrime 4.1 | Best Business Software for SMBs in India. https://tallysolutions.com/.
(11) Download Accounting Software, Download ERP Software | Tally.ERP 9.com. https://www.tally.erp9.com/downloads.html.
(12) Data Exchange Between Branches | Synchronisation & Snapshot Exchange. https://help.tallysolutions.com/tally-prime/data-exchange-tally-prime/data-synchronisation-tally/.
(1) On-chain Governance Proposals: Engaging with Your Token Holders. https://www.unvest.io/blog/on-chain-governance-proposals-engaging-with-your-token-holders.
(2) [FINAL] OP Governance Analytics Dashboard - ARCHIVED Mission Proposals .... https://gov.optimism.io/t/final-op-governance-analytics-dashboard/6171?page=2.
(3) Top Project Management Dashboard Examples & Templates - datapine. https://www.datapine.com/blog/project-management-dashboards-examples-and-templates/.
""")
