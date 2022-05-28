from brownie import FundMe, network, config, MockV3Aggregator
from .helpful_scripts import get_account


def deploy_fund_me():
    # Get account
    account = get_account()

    # Deploy contract and publish source code
    # Pass the price feed address to out contract
    # If deploy to persistent network like rinkeby, use associated address
    # Else, deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks....")
        mock_aggregator = MockV3Aggregator.deploy(
            18, 20000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print("Mocks Deployed")

    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
