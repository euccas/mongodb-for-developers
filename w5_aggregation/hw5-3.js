use test
db.grades.aggregate([ 
	{$unwind: "$scores"}, 
	{$match: {$or: [{"scores.type": "homework"}, {"scores.type": "exam"}]}}, 
	{$group: 
		{_id: {class_id: "$class_id", student_id: "$student_id"}, 
		 average: {$avg: "$scores.score"}
		}
	}, 
	{$group: 
		{_id: "$_id.class_id", average: {$avg: "$average"} }
	}, 
	{$sort: {average: -1}} 
])