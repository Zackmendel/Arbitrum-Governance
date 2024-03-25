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
  - [Introduction](#wsj-s-crypto-terrorism-claims-under-scrutiny-after-on-chain-analysis)
  - [Sam's Findings Using Flipsidecrypto Data](#sam-s-findings-using-flipsidecrypto-data)
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
