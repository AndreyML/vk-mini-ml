from typing import Optional
import pandas as pd


def write_preds(
    preds: pd.DataFrame, folder_path: str, submit_name: Optional[str] = "submission"
) -> None:
    ans = []
    preds = preds[preds["user_id"] != preds["item_id"]]
    for user in preds.user_id.unique():
        ans.append(
            f'{user}: {list(preds[preds["user_id"]==user].item_id)[:10]}'.replace(
                "[", ""
            ).replace("]", "")
        )
    with open(folder_path + f"{submit_name.txt}", "w") as fout:
        print("\n".join(ans), file=fout)
