select used_goods_board.title,used_goods_board.board_id,reply_id,used_goods_reply.writer_id,used_goods_reply.contents,date_format(used_goods_reply.created_date,'%Y-%m-%d') as created_date
from used_goods_board,used_goods_reply
where used_goods_board.board_id = used_goods_reply.board_id and
date_format(used_goods_board.created_date,'%Y-%m') = '2022-10'
order by used_goods_reply.created_date, used_goods_board.title