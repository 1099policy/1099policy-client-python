import ten99policy

# -----------------------------------------------------------------------------------*/
# Creating a quote
#-----------------------------------------------------------------------------------*/

resource = ten99policy.Quotes.create(
    job_id="jb_jsb9KEcTpc",
    contractor_id="cn_yJBbMeq9QA",
    coverage_type="general"
)

# -----------------------------------------------------------------------------------*/
# Updating a quote (replace xxx with an existing quote id)
#-----------------------------------------------------------------------------------*/

resource = ten99policy.Quotes.modify('en_C9Z2DmfHSF',
    name='Mechanic',
)

# -----------------------------------------------------------------------------------*/
# Fetching the list of quotes
#-----------------------------------------------------------------------------------*/

resource = ten99policy.Quotes.list()

# -----------------------------------------------------------------------------------*/
# Retrieving a quote (replace xxx with an existing quote id)
#-----------------------------------------------------------------------------------*/

resource = ten99policy.Quotes.retrieve('en_C9Z2DmfHSF')

print(resource)
