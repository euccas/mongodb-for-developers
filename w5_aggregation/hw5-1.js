db.posts.aggregate(
   { $project: 
	{ comments: 1 }
   }, 
   { $unwind: "$comments" }, 
   { $project: 
        {"comments.author": 1}
   },
   { $group: 
        { _id: "$comments.author", 
          num_authors: { $sum: 1 }
        }
   }, 
   { $sort: {num_authors: -1}
   } 
)
