use test
db.zips.aggregate([
    {$match: 
        {$or: [{state: "CA"}, {state: "NY"}]} 
    }, 
    {$group: {_id: "$city", population: {$sum: "$pop"},}}, 
    {$project: {_id: 1, population: 1,}}, 
    {$sort: {population: -1}}, 
    {$match: {population: {$gt: 25000} }}, 
    {$group: { _id: "$state" , popAvg: {$avg: "$population"}  }} 
])