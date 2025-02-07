class Subscription():
    def __init__(self, subscription_plan_name):
        self.subscription_plan_name = subscription_plan_name

    def has_professional_access(self):
        return self.subscription_plan_name == 'professional'

    def has_premium_access(self):
        return self.subscription_plan_name == 'premium'
