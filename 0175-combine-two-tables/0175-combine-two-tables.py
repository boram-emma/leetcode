import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    merged = person.merge(
        address[['personId', 'city', 'state']],
        on = 'personId',
        how = 'left'
    )

    return merged[['firstName', 'lastName', 'city', 'state']]
