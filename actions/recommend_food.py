from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

DATABASE = [
            # "bún đậu mắm tôm",
            # "bún đậu nước mắm",
            # "bún cá",
            # "bún hải sản",
            # "cơm văn phòng",
            # "cơm sườn",
            # "xôi",
            # "bún ốc",
            # "mì vằn thắn",
            # "hủ tiếu",
            # "bún chả",
            # "bún ngan",
            # "ngan xào tỏi",
            # "bún bò huế",
            # "mì tôm hải sản",
            # "bánh mì trứng xúc xích rắc thêm ít ngải cứu",
            # "bánh mì trứng",
            "ăn gì cũng được",
            "lá ngón"]


class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_recommend"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food = []
        for i in range(2):
            food_number = random.randrange(len(DATABASE))
            food.append(DATABASE[food_number])

        dispatcher.utter_message(
            text="Em nghĩ hôm nay anh chị có thể thử món '{}' ạ".format(food[0], food[1]))

        return []
