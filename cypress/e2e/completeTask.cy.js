describe('Complete Task', () => {

    it('should complete task', () => {

        cy.visit('http://127.0.0.1:5001')

        cy.contains('Complete').click()

    })
})