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
  st.image("https://cryptoast.fr/wp-content/uploads/2023/03/airdrop-arbitrum-enfin-la-projet-devoile-dao-dans-meme-temps.jpg")
  st.header("Navigation:")
  st.markdown("""
  - [Introduction](#introduction)
    - [Arbitrum](#arbitrum)
    - [Arbitrum Governance](#arbitrum-governance)
    - [Importance of Governance](#importance-of-governance)
    - [Community Participation](#community-participation)
    - [Differences Between Tally, Karma and Snapshot](#differences-between-tally-karma-and-snapshot)
  - [Overview](#overview)
  - [1. ON-CHAIN PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE(Compared To Karma and Tally)](#1-on-chain-proposal-and-voting-stats-of-arbitrum-governance-compared-to-karma-and-tally)
    - [Who publishes proposals most often](#Who-publishes-proposals-most-often)
  - [Which categories of users take part more often.](#Which-categories-of-users-take-part-more-often)
  - [2. SNAPSHOT PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE](#2-snapshot-proposal-and-voting-stats-of-arbitrum-governance)
    - [Which categories of users take part more often](#which-categories-of-users-take-part-more-often)
  - [3. Data Sources](#data-sources)
      - [Onchain](#onchain)
      - [Snapshot](#snapshot)
  - [CONCLUSION](#conclusion)
  """)

st.markdown(f'<h1 style="background-image:url(https://www.tbstat.com/wp/uploads/2023/03/20230315_Arbitrum_airdrop-1200x675.jpg?isSafari=false&isMobile=true);font-weight:bold;font-family:Georgia;font-size:50px;text-align:center;text-shadow: 5px 5px black;color:#FFFFFF;box-shadow: 3px 3px black;">{"Arbitrum Governance Participation Analysis."}</h1>', unsafe_allow_html=True)
# st.markdown(f'<h1 style="background-image:url(https://www.tbstat.com/wp/uploads/2023/03/20230315_Arbitrum_airdrop-1200x675.jpg?isSafari=false&isMobile=true);font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"Arbitrum Governance Participation Analysis."}</h1>', unsafe_allow_html=True)

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

cola, colb, colc = st.columns(3, gap='large')   #st.columns([1,3,1])
with colb:
  st.header(":blue[INTRODUCTION]")

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
""")


st.warning('Please go through the information in the expander below for a deeper understanding of the data used for this analysis.', icon="⚠️")
with st.expander("See Overall Proposal Id Stats SQL"):
  st.markdown("""
  - On-chain data about holders and ARB balance of holders were made based on the net transfers per wallet. This has a problem of not properly capturing users who has locked their tokens in a contract and does not directly hold the token in their wallet. For cases of accuracy, data from Arbiscan.io is used. This does not affect the delegates and voting power of delegates.
  - Snapshot uses a snapshot of token balances to get the voting power of voters and delegates, so values from that of the on-chain analysis applies to it also.

  """)
# with st.expander("See Overall Proposal Id Stats SQL"):


cola, colb, colc = st.columns([0.5,3,0.5]) #st.columns(3, gap='large')   #st.columns([1,3,1])
with colb:
  st.header(":blue[Differences Between Tally, Karma and Snapshot]")


st.markdown("""
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

In summary, **Tally** provides on-chain voting, **Karma** focuses on gasless off-chain voting, and **Snapshot** combines off-chain voting with decentralized storage. Choose the platform that aligns best with your project's goals and user preferences. 🗳️✨
""")

cola, colb, colc = st.columns(3, gap='large')   #st.columns([1,3,1])
with colb:
  st.header(":blue[Overview]")


st.markdown("""
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

st.markdown(f'<h1 style="background-image:url(https://www.tbstat.com/wp/uploads/2023/03/20230315_Arbitrum_airdrop-1200x675.jpg?isSafari=false&isMobile=true);font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"1. ON-CHAIN PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE(Compared To Karma and Tally)."}</h1>', unsafe_allow_html=True)

# st.markdown("""
## :red[1. ON-CHAIN PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE(Compared To Karma and Tally)]
# """)


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
- **TOTAL HOLDERS:** This represents the number of holders obtained from the ARB token contract [page](https://arbiscan.io/token/0x912ce59144191c1204e64559fe8253a0e49e6548).
- **NON-VOTERS:** This figure is obtained by subtracting the total number of voters from the total number of wallets that have ever voted on-chain.
- **NON-VOTING HOLDERS:** These are holders with a balance based on on-chain data who have not participated in on-chain governance. This group comprises the largest subset after total holders and non-voters. This figure indicates a concerning lack of engagement.
- **HOLDERS (bal > 0):** These are users with a balance greater than zero in their wallets. It's important to note that these values are estimates derived from on-chain data. Delegator and delegate ARBs are locked in a contract and do not reflect as a balance in their wallets. Nonetheless, this category constitutes the largest subset among all holder distribution statistics.
- **DELEGATES:** These are wallets to which tokens have been delegated for voting purposes.
- **GHOST DELEGATES:** These are delegates who have received delegations but have never participated in any on-chain voting. They represent a significant proportion (62%) of the delegates in the ARB governance.
- **VOTERS:** These are wallets that have engaged in voting activities on the Arbitrum governance platform.
- **NON-DELEGATE VOTERS:** This refers to a small portion of voters who are not delegates but are actively participating in Arbitrum governance.
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
- SQL credits for this chart go to [PANDA](https://flipsidecrypto.xyz/panda/dashboards), a data analyst at Flipside Crypto, for their work on [Voting Power on ARB Foundation](https://flipsidecrypto.xyz/panda/arbitrum-voting-power-on-arb-foundation-MpnxHx?tabIndex=4).

- This distribution was strategically organized based on the amount of ARBs delegated and the number of delegators, yielding insightful findings.
- Regarding the ARBs delegated, a significant number of delegates (specifically the top 50) received substantial delegations exceeding 1000 ARBs, constituting the majority of the ARBs delegated to them.
- An offsetting factor to the above finding is that, based on users delegating, most wallets delegated less than 100 ARBs to the delegates.
- This suggests that the majority of the voting power of these delegates originated from a select few whales, indicating a potential centralization issue.
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
             height=400)
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

st.markdown(f'<h1 style="background-image:url(https://www.tbstat.com/wp/uploads/2023/03/20230315_Arbitrum_airdrop-1200x675.jpg?isSafari=false&isMobile=true);font-weight:bold;font-family:Georgia;font-size:30px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"2. SNAPSHOT PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE."}</h1>', unsafe_allow_html=True)

# st.markdown("""
# ## :red[2. SNAPSHOT PROPOSAL AND VOTING STATS OF ARBITRUM GOVERNANCE]
# """)


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

st.markdown("""
### COMMENTS
- On Snapshot, a total of 6.96k proposals proposed by 5.8k unique proposers has been voted upon on the Arbitrum governance. COmparing this value to that of Tally and Karma, it is seen that a lot more users engage more with snapshot.
- A total of approximately 4.93million votes has been made by 279.3k voters out of which a significant portion (3.05mill) voted in favor of the proposals while a smaller number voted against and some abstained from picking a choice.
- Daily votes on Arbitrum Governance is seen to have peaked on Oct 7th 2023. The growth of voters participation is seen to be seriously high in recent days indicationg more interest of the users to participate on governance activities, this is a very good sign.
""")

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
### :blue[Who publishes proposals most often(Snapshot)?]
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

# -------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
### :blue[Which categories of users take part more often(Snapshot)?]
""")

csvi = pd.read_csv("csv_data/Voters_Participation_by_Votes(snapshot).csv")
csvj = pd.read_csv("csv_data/Voters_Participation_by_days(snapshot).csv")

col_1, col_2 = st.columns(2, gap='large')
with col_1:
  fig_2a = px.bar(csvi, x="PARTICIPATION", y="VOTERS", title="Voters Participation by Votes(Snapshot)", height=500, color="PARTICIPATION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

with col_2:
  fig_2a = px.bar(csvj, x="PARTICIPATION", y="VOTERS", title="Voters Participation by Days(Snapshot)", height=500, color="PARTICIPATION") 
# log_y=True)
  fig_2a.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2a, use_container_width=True)

st.markdown("""
### COMMENTS
- Unlike the onchain stats, more voters are seen to be returnees with the most voters voting more than 10 times and spending more than five days in total in their voting history. This shows that a lot more users are involved in using Snapshot for voting. Probably cos of its convenience.
""")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(f'<h1 style="background-image:url(https://www.tbstat.com/wp/uploads/2023/03/20230315_Arbitrum_airdrop-1200x675.jpg?isSafari=false&isMobile=true);font-weight:bold;font-family:Georgia;font-size:50px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"3. Data Sources."}</h1>', unsafe_allow_html=True)


# st.markdown("""
# ## :red[3. Data Sources]
# """)


# --------------------------------------------------------------------------------

st.markdown("""
### :blue[Overall Proposal Id On-chain Stats on Arbitrum]
""")

csv1 = pd.read_csv("csv_data/Overall_Proposal_Id_Stats.csv", on_bad_lines='skip')

st.dataframe(csv1)

# fig_1 = px.bar(csv1, x="DATE_CREATED", y=["FOR", "AGAINST", "ABSTAIN"], title="Daily Marketcap of Arb Token", barmode='group', height=500) 
# # log_y=True)
# fig_1.update_layout(hovermode="x unified")
# # Add Scatter plot
# fig_1.add_scatter(x=csv1['DATE_CREATED'], y=csv1['TOTAL_VOTES'], name="Total Votes", line_color="red")
# # fig_1.add_scatter(x=csv4['timestamp'], y=csv4['circulating_supply'], name="Circulating Supply", line_color="red")
# st.plotly_chart(fig_1, use_container_width=True)



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

st.markdown(f'<h1 style="background-image:url(https://www.tbstat.com/wp/uploads/2023/03/20230315_Arbitrum_airdrop-1200x675.jpg?isSafari=false&isMobile=true);font-weight:bold;font-family:Georgia;font-size:50px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"4. CONCLUSIONS."}</h1>', unsafe_allow_html=True)

st.markdown("""
- In conclusion, the analysis into Arbitrum governance has provided valuable insights into the dynamics of onchain voting and the distribution of governance power within the ecosystem. With 29 proposals put forth by 9 unique proposers, the governance process has seen active participation, albeit with some notable trends.
- One striking observation is the disparity between the total circulating ARBs and the amount available for voting, which stands at just 12%. This limited pool for decision-making underscores the need for broader participation and engagement in governance processes.
- The distribution of voters reveals interesting patterns, with a significant portion favoring proposals while others either voted against or abstained. However, the concentration of voting power among a few delegates, primarily supported by larger delegations from whales, raises concerns about centralization within the governance structure.
- Furthermore, the dominance of certain users, such as 0xfrisson, in proposal submissions highlights potential areas for diversification and inclusivity within the governance framework.
- Examining user behavior, it becomes evident that while there is a considerable number of repeat voters, overall commitment to Arbitrum governance appears relatively low, with many participants engaging sporadically and for short durations. Bridging and dex users emerge as prominent voters, raising questions about their motivations and broader participation across different chains.
- The contrast between onchain and offchain voting patterns suggests that platforms like Snapshot are gaining traction, possibly due to their convenience and accessibility, attracting a more diverse range of participants.
- In moving forward, addressing centralization concerns, enhancing voter engagement, and promoting inclusivity should be key priorities for strengthening the integrity and effectiveness of Arbitrum governance. Moreover, continued analysis and monitoring of voting behaviors will be essential for guiding future improvements and ensuring a more robust and representative governance ecosystem.
""")

st.markdown(f'<h1 style="background-image:url(https://www.tbstat.com/wp/uploads/2023/03/20230315_Arbitrum_airdrop-1200x675.jpg?isSafari=false&isMobile=true);font-weight:bold;font-family:Georgia;font-size:50px;text-align:center;text-shadow: 5px 5px black;color:#f23a7d;box-shadow: 3px 3px black;">{"5. REFERENCES."}</h1>', unsafe_allow_html=True)

st.markdown("""
1. [For decentralized governance on Ethereum, why is Snapshot considered ....]( https://ethereum.stackexchange.com/questions/127331/for-decentralized-governance-on-ethereum-why-is-snapshot-considered-off-chain.)
2. [Snapshot Polls | Tally Docs.]( https://docs.tally.xyz/education/governance-frameworks/snapshot-polls.)
3. [What's the difference between Tally vs Snapshot? : r/dao - Reddit.]( https://www.reddit.com/r/dao/comments/sbjbpn/whats_the_difference_between_tally_vs_snapshot/.)
4. [Tally - Run DAOs onchain.]( https://www.tally.xyz/.)
5. [Data Exchange Between Branches | Synchronisation & Snapshot Exchange.]( https://help.tallysolutions.com/tally-prime/data-exchange-tally-prime/data-synchronisation-tally/.)
6. [On-chain Governance Proposals: Engaging with Your Token Holders.]( https://www.unvest.io/blog/on-chain-governance-proposals-engaging-with-your-token-holders.)
7. [FINAL OP Governance Analytics Dashboard - ARCHIVED Mission Proposals ....]( https://gov.optimism.io/t/final-op-governance-analytics-dashboard/6171?page=2.)
8. [Top Project Management Dashboard Examples & Templates - datapine.]( https://www.datapine.com/blog/project-management-dashboards-examples-and-templates/.)
9. [Voting Power on ARB Foundation](https://flipsidecrypto.xyz/panda/arbitrum-voting-power-on-arb-foundation-MpnxHx?tabIndex=4)
""")

