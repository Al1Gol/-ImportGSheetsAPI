import React from 'react'

const OrdersItem = ({order}) => {
    return (
        <tbody>
            <tr>
                <td>{order.id}</td>
                <td>{order.order}</td>
                <td>{order.sum_dol}</td>
                <td>{order.sum_rub}</td>
                <td>{order.delivery_time}</td>
            </tr>
        </tbody>
    )
}

const OrdersList = ({orders}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        №
                    </th>
                    <th>
                        заказ №
                    </th>
                    <th>
                        стоимость,$
                    </th>
                    <th>
                        стоимость,rub.
                    </th>
                    <th>
                        срок поставки
                    </th>
                </tr>
            </thead>
            {orders.map((order) => <OrdersItem order={order}/>)}
        </table>
    )
}

export default OrdersList