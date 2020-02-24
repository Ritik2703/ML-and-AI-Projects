"""
This is using the quantopian libraries to execute
a test on how the sentiment on social media correlates
to the action of price movement on the stock market.

Social Media Sentiment vs. Stock Market Price Action

Because this is using the Quantopian libraries we need
to run this script in Quantopian's IDE at quantopian.com
"""



from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.factors import AverageDollarVolume
from quantopian.pipeline.data.accern import alphaone_free

def initialize(context):
    attach_pipeline(make_pipeline(), 'pipline')
    schedule_function(my_rebalance, date_rules.every_day())



######################
#       Scanner      #
#    Main Pipeline   #
######################
def make_pipeline():
    dollar_volume_pipe = AverageDollarVolume(window_length = 20)
    is_liquid_pipe = dollar_volume_pipe.top(1000)

    impact = alphaone_free.impact_score.latest
    sentiment = alphaone_free.article_sentiment.latest

    return Pipeline( columns =
                    {'impact': impact,
                    'sentiment': sentiment},
                    screen = is_liquid_pipe)


######################
#  Trading Strategy  #
#     Passing In     #
#    Main Pipeline   #
######################
def before_trading_start(context, data):
    main_pipe = pipeline_output('pipeline')
    # Trading Strategy
    context.longs = main_pipe[(main_pipe['impact'] == 100) & (main_pipe['sentiment'] > 0.75)].index.tolist()

    context.shorts = main_pipe[(main_pipe['impact'] == 100) & (main_pipe['sentiment'] < -0.5)].index.tolist()

    context.long_weight, context.short_weight = my_compute_weights(context)

######################
# Account Allocation #
#    Set User Cost   #
######################
def my_compute_weights(context):
    """
    if else statements are filtering for zero division errors:
    """
    if len(context.longs) == 0:
        long_weight = 0
    else:
        long_weight = 0.5 / len(context.longs)

    if len(context.shorts) == 0:
        short_weight = 0
    else:
        short_weight = 0.5 / len(context.shorts)

    return (long_weight, short_weight)




######################
#  Execute Strategy  #
# Garbage Collection #
######################
"""
my_rebalance cleans the pipelines as data changes and
exits positions that no longer meets the requirements
specified by the Main PipeLine.
"""
def my_rebalance(contex, data):
    for security in context.portfolio.positions:
        if security not in context.longs and security not in context.shorts and data.can_trade(security):
            order_target_percent(security, 0)

    for security in context.longs:
        if data.can_trade(security):
            order_target_percent(security, context.long_weight)

    for security in context.shorts:
        if data.can_trade(security):
            order_target_percent(security, context.short_weight)
