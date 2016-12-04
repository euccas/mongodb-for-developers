db.messages.aggregate( 
	{$project: {"headers.To": 1, "headers.From": 1}}, 
	{$group: {_id: {"from": "$headers.From", "to": "$headers.To"}, 
	 num_comm: {$sum: 1} }}, 
	{$sort: {num_comm: -1}}
)